from django.contrib import admin
from .models import Device, Room, AvailableAutomation, HVAC

admin.site.register(Device)
admin.site.register(Room)
admin.site.register(AvailableAutomation)
admin.site.register(HVAC)
