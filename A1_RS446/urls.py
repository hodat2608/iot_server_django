from django.urls import path
from A1_RS446.views import detail_date,detail_data

urlpatterns = [
    path('ccai0028_detail_date/<int:id>/', detail_date, name= 'ccai0028_detail_date'),
    path('ccai0028_detail_data/<int:id>/', detail_data, name= 'ccai0028_detail_data'),
]