from django.urls import path
from Tam_Sat_M100_A75 import views
app_client = 'ccai0004'
urlpatterns = [
    path(f'{app_client}_detail_date/<int:id>/', views.detail_date, name= f'{app_client}_detail_date'),
    path(f'{app_client}_detail_data/<int:id>/', views.detail_data, name=f'{app_client}_detail_data'), 
    path(f'{app_client}_chart/<int:id>/', views.chart_date, name=f'{app_client}_chart'),
    path(f'{app_client}_search/', views.search_date_lot, name=f'{app_client}_search'),
    path(f'{app_client}_delete_selected_records/', views.delete_selected_records, name=f'{app_client}_delete_selected_records'),
    path(f'{app_client}_detail_data_realtime/<int:id>/', views.detail_data_realtime, name=f'{app_client}_detail_data_realtime'),
    path(f'{app_client}_chart_data_realtime/<int:id>/', views.chart_data_realtime, name=f'{app_client}_chart_data_realtime'),
]
