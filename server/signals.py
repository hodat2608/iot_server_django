from django.db.models.signals import post_save
from django.dispatch import receiver
from server.models import server_test
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

@receiver(post_save, sender=server_test)
def update_client_data(sender, instance, created, **kwargs):
    if created:
        return
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "client_data_group",
        {
            "type": "update_client_data",
            "client_data": {
                "id": instance.id,
                "name_client": instance.name_client,
                "line": instance.line,
                "port": instance.port,
                "host": instance.host,
                "status": instance.status
            }
        }
    )
