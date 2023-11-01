from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from .models import Device, TemperatureReading, HumidityReading
from .serializers import DeviceSerializer, TemperatureReadingSerializer, HumidityReadingSerializer
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import Http404
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import io,base64


class DeviceListCreateView(APIView):
    """
    List all devices or create a new device.
    """
    def get(self, request, format=None):
        devices = Device.objects.all()
        serializer = DeviceSerializer(devices, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DeviceRetrieveDeleteView(APIView):
    """
    Retrieve or delete a device instance.
    """
    def get_object(self, uid):
        try:
            return Device.objects.get(uid=uid)
        except Device.DoesNotExist:
            raise Http404

    def get(self, request, device_uid, format=None):
        device = self.get_object(device_uid)
        serializer = DeviceSerializer(device)
        return Response(serializer.data)

    def delete(self, request, device_uid, format=None):
        device = self.get_object(device_uid)
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([AllowAny])
def device_readings(request, uid, parameter):
    start_on = request.query_params.get('start_on')
    end_on = request.query_params.get('end_on')

    if not all([start_on, end_on]):
        return Response({'error': 'start_on and end_on query parameters are required'},
                        status=status.HTTP_400_BAD_REQUEST)
    device = get_object_or_404(Device, uid=uid)

    if parameter == 'temperature':
        readings = TemperatureReading.objects.filter(device=device, timestamp__range=[start_on, end_on])
        serializer = TemperatureReadingSerializer(readings, many=True)
    elif parameter == 'humidity':
        readings = HumidityReading.objects.filter(device=device, timestamp__range=[start_on, end_on])
        serializer = HumidityReadingSerializer(readings, many=True)
    else:
        return Response({'error': 'Invalid parameter. Only temperature or humidity are allowed'},
                        status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.data)


def device_graph(request):
    device_uid = request.GET.get("uid")

    try:
        device = Device.objects.get(uid=device_uid)
        temperature_readings = TemperatureReading.objects.filter(device=device)
        humidity_readings = HumidityReading.objects.filter(device=device)
    except Device.DoesNotExist:
        return render(request, "error.html", {"error_message": "Device does not exist"})

    timestamps = [reading.timestamp for reading in temperature_readings]
    temperatures = [reading.temperature for reading in temperature_readings]
    humidities = [reading.humidity for reading in humidity_readings]

    #Creating the plot
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, temperatures, label="Temperature", marker=".")
    plt.plot(timestamps, humidities, label="Humidity", marker=".")
    plt.xlabel("Timestamp")
    plt.ylabel("Value")
    plt.legend()
    plt.title(f"Temperature and Humidity Readings - {device.name}")
    plt.xticks(rotation=45)
    plt.savefig('graph.png')
    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()
   
    
    graph = base64.b64encode(buf.read()).decode("utf-8")
    
    return render(request, "graph.html", {"graph": graph})
