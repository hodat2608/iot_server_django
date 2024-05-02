from django.urls import path
from server.views import show_all_client,update_client_status,generate_client

urlpatterns = [
    path('client/', show_all_client, name= 'client'),
    # path('client_status/', sse_update_client_status, name= 'client_status'),
    path('generate_client/', generate_client, name= 'generate_client'),
]
