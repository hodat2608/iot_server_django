import socket
import threading
import time
from celery import Celery
from django.conf import settings
from server.models import server_test

# Cấu hình Celery
app = Celery('x75_m100')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

SERVER_HOST = "10.7.11.28"
SERVER_PORTS = [1122]
BUFFER_SIZE = 4096
HEARTBEAT_INTERVAL = 5
SEPARATOR = "<SEPARATOR>"

def handle_client_connection(client_socket, address):
    print(f"[+] {address} is connected.")
    print(f"[*] Connected successfully with client {address[0]}:{address[1]}")
    try:
        while True:
            client_socket.sendall(b"heartbeat")
            time.sleep(HEARTBEAT_INTERVAL)
    except (socket.error, ConnectionResetError):
        print(f"[-] {address} disconnected.")
        update_status(address[0], False)

def start_server(port):
    while True:
        s = socket.socket()
        try:
            s.bind((SERVER_HOST, port))
            s.listen(5)
            print(f"[*] Listening as {SERVER_HOST}:{port}\n")
            while True:
                client_socket, address = s.accept()
                update_status(address[0], True)
                client_thread = threading.Thread(target=handle_client_connection, args=(client_socket, address))
                client_thread.start()
        except socket.error:
            print(f"[-] Failed to bind to port {port}. Retrying...")
            time.sleep(5)
        finally:
            s.close()

def start_servers():
    for port in SERVER_PORTS:
        server_thread = threading.Thread(target=start_server, args=(port,))
        server_thread.start()

def update_status(ip, status):
    try:
        client = server_test.objects.get(host=ip)
        client.status = status
        client.save()
    except server_test.DoesNotExist:
        pass

def check_ip_exist(ip):
    return server_test.objects.filter(host=ip).exists()

@app.task
def periodic_check():
    ip_to_check = "10.7.11.22"
    while True:
        if check_ip_exist(ip_to_check):
            update_status(ip_to_check, True)
            print(f"Trạng thái HOST {ip_to_check}: ONLINE")
        else: 
            update_status(ip_to_check, False)
            print(f"Trạng thái HOST {ip_to_check}: OFFLINE")
        time.sleep(5)

app.conf.beat_schedule = {
    'periodic-check-every-5-seconds': {
        'task': 'x75_m100.celery.periodic_check',
        'schedule': 5.0,
    },
}


# {% with view_name=client.name_client %}
# <td><a href="{% url view_name client.id %}">View Data</a></td>
# {% endwith %}