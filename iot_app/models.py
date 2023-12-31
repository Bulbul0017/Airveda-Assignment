from django.db import models

# Create your models here.
class Device(models.Model):
    uid = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class TemperatureReading(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "%s %s" %(self.temperature, self.timestamp)

class HumidityReading(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "%s %s" %(self.humidity, self.timestamp)