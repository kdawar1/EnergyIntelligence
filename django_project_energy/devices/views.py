from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Device, Room, AvailableAutomation, HVAC

def home(request):
    context = {
        'hvacs': HVAC.objects.all(),
        'rooms': Room.objects.all(),
        'devices': Device.objects.all(),
        'autos': AvailableAutomation.objects.all()
    }
    return render(request, 'devices/home.html', context)


def about(request):
    return render(request, 'devices/about.html', {'title': 'About'})

def test_update(request, pk):
    device = get_object_or_404(Device, pk=pk)
    if device.is_on == 'On':
        device.is_on = 'Off'
    else:
        device.is_on = 'On'
    device.save()
    messages.success(request, '{} was turned {} successfully'.format(device.device_name, device.is_on))
    return redirect('room-detail', pk=device.room.pk)

### Device View
class UserDeviceListView(LoginRequiredMixin, ListView):
    model = Device
    template_name = 'devices/user_devices.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'devices'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Device.objects.filter(room__author=user).order_by('-date_added')


class DeviceDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Device

    def test_func(self):
        device = self.get_object()
        if self.request.user == device.room.author:
            return True
        return False

class DeviceCreateView(LoginRequiredMixin, CreateView):
    model = Device
    fields = ['device_name', 'sensor','sensor_ID', 'room', 'is_entertainment', 'is_on']

    def form_valid(self, form):
        form.instance.room.author = self.request.user
        return super().form_valid(form)


class DeviceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Device
    fields = ['device_name', 'sensor','sensor_ID','room', 'is_entertainment', 'is_on']

    def form_valid(self, form):
        form.instance.room.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        device = self.get_object()
        if self.request.user == device.room.author:
            return True
        return False


class DeviceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Device
    success_url = '/'

    def test_func(self):
        device = self.get_object()
        if self.request.user == device.room.author:
            return True
        return False

### Room View
class UserRoomListView(LoginRequiredMixin, ListView):
    model = Room
    template_name = 'devices/user_rooms.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'rooms'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Room.objects.filter(author=user)

class RoomDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Room

    def test_func(self):
        room = self.get_object()
        if self.request.user == room.author:
            return True
        return False


class RoomCreateView(LoginRequiredMixin, CreateView):
    model = Room
    fields = ['room_name', 'room_type']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RoomUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Room
    fields = ['room_name', 'room_type']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        room = self.get_object()
        if self.request.user == room.author:
            return True
        return False


class RoomDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Room
    success_url = '/'

    def test_func(self):
        room = self.get_object()
        if self.request.user == room.author:
            return True
        return False


##### Automation view

class UserAutoListView(LoginRequiredMixin, ListView):
    model = AvailableAutomation
    template_name = 'devices/user_autos.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'autos'
    # paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return AvailableAutomation.objects.filter(device__room__author=user)

###### HVAC view

def hvac_update(request, pk):
    hvac = get_object_or_404(HVAC, pk=pk)
    if hvac.power == 'Power Saver':
        hvac.power = 'Normal'
    else:
        hvac.power = 'Power Saver'
    hvac.save()
    messages.success(request, 'HVAC {} was turned to {} mode successfully'.format(hvac.pk, hvac.power))
    return redirect('blog-home')
