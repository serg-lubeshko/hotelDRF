from rest_framework import generics, permissions

from backend.hotel.models import HotelRooms, BookingRoom
from api.hotel.serializer import (HotelRoomsSerializers, BookingRoomListSerializer, BookingRoomSerializer)


class HotelRoomsList(generics.ListAPIView):  # Any user can see the numbers
    '''Список номеров отеля -List room hotel'''
    permission_classes = [permissions.AllowAny]
    queryset = HotelRooms.objects.all()
    serializer_class = HotelRoomsSerializers


class BookingRoomList(generics.ListAPIView):
    """Список забронированных номеров"""
    permission_classes = [permissions.IsAdminUser]
    queryset = BookingRoom.objects.all()
    serializer_class = BookingRoomListSerializer


class BookingRoomRecord(generics.CreateAPIView):
    """Запись брони в БД"""
    permission_classes = [permissions.AllowAny]
    queryset = BookingRoom.objects.all()
    serializer_class = BookingRoomSerializer #BookinRoomSerializer
