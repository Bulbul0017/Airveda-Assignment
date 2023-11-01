from django.urls import path
from . import views
from iot_app.views import device_readings 



urlpatterns = [
    path('devices/', views.DeviceListCreateView.as_view(), name='device-list-create'),
    path('devices/<str:device_uid>/', views.DeviceRetrieveDeleteView.as_view(), name='device-retrieve-delete'),
    path('devices/<str:uid>/readings/<str:parameter>/', device_readings, name='device-readings'),
    path('devices-graph/',views.device_graph,name='device-graph'),
]