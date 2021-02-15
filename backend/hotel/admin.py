from django.contrib import admin
from .models import HotelRooms, HotelFields, RatingRooms, BookingRoom


class HotelFieldsAdmin(admin.StackedInline):
    model = HotelFields
    extra = 1
    show_change_link = True


class RatingRoomsAdmin(admin.StackedInline):
    model = RatingRooms
    extra = 1
    show_change_link = True


@admin.register(HotelRooms)
class HotelRoomsAdmin(admin.ModelAdmin):
    """Номер отеля"""
    list_display = ('title', 'desc')
    search_fields = ('title',)
    inlines = [HotelFieldsAdmin, RatingRoomsAdmin]


@admin.register(BookingRoom)
class BookingRoomAdmin(admin.ModelAdmin):
    """Номер отеля"""
    list_display = ('name', 'phone', 'entry_date', 'depart_date', 'adult', 'children')
    search_fields = ('name',)

