from django.urls import path
from x75_m100.views import delete_selected_records,detail_date,detail_data,add_category_lddk,chart_date,detail_date_show_all,search_date_lot,sse_update_data,detail_data_realtime

urlpatterns = [
    path('ccai0015_detail_date/<int:id>/', detail_date, name='ccai0015_detail_date'),
    path('ccai0015_detail_date_show_all/<int:id>/', detail_date_show_all, name='ccai0015_detail_date_show_all'),
    path('ccai0015_detail_data/<int:id>/', detail_data, name='ccai0015_detail_data'),
    path('ccai0015_detail_data_realtime/<int:id>/', detail_data_realtime, name='detail_data_realtime'),
    path('ccai0015_nhap_lddk/<int:id>/', add_category_lddk, name='ccai0015_nhap_lddk'),
    path('ccai0015_chart/<int:id>/', chart_date, name='ccai0015_chart'),
    path('ccai0015_search/', search_date_lot, name='ccai0015_search'),
    path('ccai0015_delete_selected_records/', delete_selected_records, name='ccai0015_delete_selected_records'),
    path('ccai0015_sse_update_data_realtime/<int:id>/', sse_update_data, name='ccai0015_sse_update_data_realtime'),
]

