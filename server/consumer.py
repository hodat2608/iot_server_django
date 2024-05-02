from channels.generic.websocket import WebsocketConsumer
from server.models import server_test
import json
import random
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from time import sleep
from channels.db import database_sync_to_async

# class ServerStatusConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         await self.accept()
#         async for event_data in self.generate_event_data():
#             await self.send(text_data=event_data)
            
#     async def generate_event_data(self):
#         while True:
#             clients = await sync_to_async(server_test.objects.all)()
#             for client in clients:
#                 data = {'id': client.id, 'status': client.status}
#                 yield json.dumps(data)

#     async def disconnect(self, close_code):
#         pass

class ServerStatusConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        for event_data in self.generate_event_data():
            self.send(text_data=event_data)
            
    def generate_event_data(self):
        while True:
            clients = server_test.objects.all()
            for client in clients:
                data = {'id': client.id, 'status': client.status}
                yield json.dumps(data)

    def disconnect(self, close_code):
        pass

    # def connect(self):
    #     self.accept()
    #     # Join a group to receive updates
    #     async_to_sync(self.channel_layer.group_add)(
    #         "status_updates",
    #         self.channel_name
    #     )
    #     # Send initial status data to client
    #     self.send_initial_status()

    # def disconnect(self, close_code):
    #     # Leave the group when disconnected
    #     async_to_sync(self.channel_layer.group_discard)(
    #         "status_updates",
    #         self.channel_name
    #     )

    # def send_initial_status(self):
    #     while True: 
    #         clients = server_test.objects.all()
    #         for client in clients:
    #             self.send_status_update(client.id, client.status)
    #         sleep(5)

    # def send_status_update(self, client_id, status):
    #     self.send(text_data=json.dumps({
    #         'type': 'status_update',
    #         'client_id': client_id,
    #         'status': status,
    #     }))

    # def status_changed(self, event):
    #     client_id = event['client_id']
    #     status = event['status']
    #     self.send_status_update(client_id, status)

    # def connect(self):
    #     self.accept() 
    #     for i in range(1000):
    #         self.send(json.dumps({'value': random.randint(-20,20)}))
    #         sleep(1)