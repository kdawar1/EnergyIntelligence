from django.urls import path, re_path
from .views import (
    DeviceDetailView,
    DeviceCreateView,
    DeviceUpdateView,
    DeviceDeleteView,
    UserDeviceListView,
    RoomDetailView,
    RoomCreateView,
    RoomUpdateView,
    RoomDeleteView,
    UserRoomListView,
    UserAutoListView,
    home,
    about,
    test_update,
    hvac_update,
)

urlpatterns = [
    path('user_devices/<str:username>/', UserDeviceListView.as_view(), name='user-devices'),
    path('new/device/', DeviceCreateView.as_view(), name='device-create'),
    path('<int:pk>/', DeviceDetailView.as_view(), name='device-detail'),
    path('<int:pk>/update/', DeviceUpdateView.as_view(), name='device-update'),
    path('<int:pk>/delete/', DeviceDeleteView.as_view(), name='device-delete'),

    path('user_rooms/<str:username>/', UserRoomListView.as_view(), name='user-rooms'),
    path('room/<int:pk>/', RoomDetailView.as_view(), name='room-detail'),
    path('new/room/', RoomCreateView.as_view(), name='room-create'),
    path('room/<int:pk>/update/', RoomUpdateView.as_view(), name='room-update'),
    path('room/<int:pk>/delete/', RoomDeleteView.as_view(), name='room-delete'),

    path('auto/<str:username>/', UserAutoListView.as_view(), name='user-autos'),
    
    #path('hvac/', hvac_details, name='user-hvacs'),
    
    path('test/<int:pk>/', test_update, name='test_update'),
    path('hvac/<int:pk>/', hvac_update, name='hvac_update'),
    path('', home, name='blog-home'),
    path('about/', about, name='blog-about'),
]
