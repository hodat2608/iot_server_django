from django.urls import path,re_path
from server.consumer import ServerStatusConsumer

websocket_urlpatterns = [
    re_path(r'ws/client_data/$', ServerStatusConsumer.as_asgi()),
]
