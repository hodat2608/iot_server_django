from django.urls import path,re_path
from A18_RS656.consumers import ChartDateRealtimeConsumer_Async,ChartDataRealtimeConsumer_Async,DetailDataRealtimeConsumer,Detail_Date_RealTime
app_websocket_client = 'ccai0019'
websocket_urlpatterns = [
    path(f'ws/realtime_chart/{app_websocket_client}/<str:date_id>/', ChartDataRealtimeConsumer_Async.as_asgi()),
    path(f'ws/detail_data_realtime/{app_websocket_client}/<str:date_id>/', DetailDataRealtimeConsumer.as_asgi()),
    path(f'ws/realtime_date_table/{app_websocket_client}/<str:client_id>/', Detail_Date_RealTime.as_asgi()),
    path(f'ws/realtime_date_chart/{app_websocket_client}/<str:id>/', ChartDateRealtimeConsumer_Async.as_asgi()),
]