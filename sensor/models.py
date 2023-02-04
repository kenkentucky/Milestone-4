from django.db import models
from django.utils import timezone
from django_filters import FilterSet, AllValuesFilter
from django_filters import DateTimeFilter, NumberFilter
# Create your models here.

    


class Room(models.Model):

    type = models.CharField(max_length=200, null = False, blank = False)
    floor = models.IntegerField()

    def __str__(self):
        return self.type

class PersonInCharge(models.Model):

    PersonName = models.CharField(max_length=200, null = False, blank = False)
    Age = models.IntegerField()
    EmployeeID = models.IntegerField()
    EmployeeRoom= models.ForeignKey(Room, blank=True, null =True, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.PersonName)

class Sensors(models.Model):
    
    SensorName = models.CharField(max_length=200, null = False, blank = False)
    person = models.ForeignKey(PersonInCharge,max_length=200, null = True, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, blank=True, null =True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.SensorName 


class TempHumid(models.Model):
    
    timestamp = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(Room, blank=True, null =True, on_delete=models.CASCADE)
    tempvalue = models.IntegerField()
    humidval = models.IntegerField()
    sensor = models.ForeignKey(Sensors, blank=True, null =True, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.sensor)

