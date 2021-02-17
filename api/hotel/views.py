from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

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

class HotelViewList(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self,request):
        rooms = HotelRooms.objects.all()
        ser = HotelRoomsSerializers(rooms)
        return Response(ser.data)

class BookingRoomRecord(APIView):
    def post(self,request):
        room =BookingRoomSerializer(data=request.data)
        if room.is_valid():
            room.save()
        return Response(status=201)

class BookingRoomRecord2(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = BookingRoom.objects.all()
    serializer_class = BookingRoomSerializer

class HotelRoomView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = HotelRooms.objects.all()
    serializer_class = HotelRoomsSerializers

class HotelDetailView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self,request, pk):
        rooms = HotelRooms.objects.filter(id=pk)
        ser = HotelRoomsSerializers(rooms, many=True)
        return Response(ser.data)