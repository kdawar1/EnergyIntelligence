from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Room(models.Model):
    ROOM_CHOICES = (
        ('Bedroom', 'Bedroom'),
        ('Bathroom', 'Bathroom'),
        ('Kitchen' , 'Kitchen'),
        ('Living Room' , 'Living Room'),
        ('Dining Room' , 'Dining Room'),
        ('Closet' , 'Closet'),
        ('Other', 'Other')
    )
    room_name = models.CharField(max_length=20)
    room_type = models.CharField(max_length=15, choices=ROOM_CHOICES)
    # date_added = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.room_name
    
    def get_absolute_url(self):
        return reverse('room-detail', kwargs={'pk': self.pk})

class Device(models.Model):
    SENSOR_CHOICES = (
        ('LIDAR', 'LIDAR'),
        ('Pressure', 'Pressure'),
        ('Temperature' , 'Temperature'),
        ('Proximity' , 'Proximity'),
        ('Ultrasonic' , 'Ultrasonic'),
        ('Flow' , 'Flow and Level'),
        ('Humidity' , 'Humidity'),
        ('IR' , 'Infrared'),
        ('Smoke' , 'Smoke, Gas and Alcohol'),
    )
    ENTERTAINMENT_CHOICE = (('Yes', 'Yes'), ('No','No'),)
    STATUS_CHOICE = (('On', 'On'), ('Off','Off'),)
    device_name = models.CharField(max_length=100)
    sensor = models.CharField(max_length=15, choices=SENSOR_CHOICES)
    date_added = models.DateTimeField(default=timezone.now)
    sensor_ID = models.CharField(max_length=30)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    is_entertainment = models.CharField(max_length=15, choices=ENTERTAINMENT_CHOICE, default='No')
    is_on = models.CharField(max_length=15, choices=STATUS_CHOICE, default = 'Off')

    def __str__(self):
        return self.device_name

    def get_absolute_url(self):
        return reverse('device-detail', kwargs={'pk': self.pk})

class AvailableAutomation(models.Model):
    TIME_CHOICES = (
        ('after_sunrise', 'Day (After sunrise)'),
        ('after_sunset', 'Night (After sunset)'),
    )
    WEATHER_CHOICES = (
        ('cloudy', 'Cloudy'),
        ('not_cloudy', 'Not Cloudy'),
    )
    ACTIVITY_CHOICES = (
        ('room_in', 'Entering the room'),
        ('room_out', 'Exiting the room'),
        ('room_in_entertainment' , 'Room in entertainment'),
        ('room_in_non_entertainment' , 'Room in non-entertainment'),
        ('room_in_sleeping', 'Sleeping'),
    )
    
    AUTO_CHOICES = (('On', 'On'), ('Off','Off'),)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    auto_avail = models.BooleanField(default=False)
    automation = models.CharField(max_length=5, choices=AUTO_CHOICES, default='Off')
    time = models.CharField(max_length=20, choices=TIME_CHOICES)
    activity = models.CharField(max_length=30, choices=ACTIVITY_CHOICES)
    weather = models.CharField(max_length=30, choices=WEATHER_CHOICES)

    def __str__(self):
        return '{} {}'.format(self.device.device_name, self.auto_avail)

    def get_absolute_url(self):
        return reverse('auto-detail', kwargs={'pk': self.pk})

class HVAC(models.Model):
    POWER_CHOICES = (('Power Saver', 'Power Saver'), ('Normal','Normal'),)
    power = models.CharField(max_length=20, choices=POWER_CHOICES, default='Power Saver')
    temp = models.IntegerField(default=72)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.power
