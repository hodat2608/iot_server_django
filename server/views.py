from django.shortcuts import render
from django.http import JsonResponse
from server.models import server_test
from django.http import StreamingHttpResponse
import json

def show_all_client(request):
    clients = server_test.objects.all()
    context = {'clients':clients}
    return render(request, 'static/index_websocket.html', context)
    

def update_client_status(request):
    clients = server_test.objects.all()
    updated_clients = [{'id': client.id, 'status': client.status} for client in clients]
    return JsonResponse({'clients': updated_clients})


# def generate_event_data():
#     clients = server_test.objects.all()
#     for client in clients:
#         yield f"data: {json.dumps({'id': client.id, 'status': client.status})}\n\n"

# def sse_update_client_status(request):
#     response = StreamingHttpResponse(generate_event_data(), content_type='text/event-stream')
#     response['Cache-Control'] = 'no-cache'
#     return response

def generate_client(request):
    if request.method == 'POST':
        name_client = request.POST.get('name_client')
        line = request.POST.get('line')
        port = request.POST.get('port')
        host = request.POST.get('host')
        client = server_test(
            name_client=name_client,
            line=line,
            port=port,
            host=host,
        )
        client.save()
        new_client = { 
            'name_client': client.name_client,
            'line': client.line,
            'port': client.port,
            'host': client.host,
            'status':client.status
            }              
        return JsonResponse(new_client)
    

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


def update_status(client_id, status):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "client_status_updates",
        {
            "type": "client.status_update",
            "id": client_id,
            "status": status
        }
    )

def your_view_function(request):
    clients = server_test.objects.all()
    for client in clients:
        # Do your operations
        # If status changes, call update_status
        update_status(client.id, client.status)

    