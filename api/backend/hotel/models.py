from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class HotelRooms(models.Model):
    """"Номер отеля"""
    title = models.CharField("НазваниЕ", max_length=250)
    desc = models.CharField("ОписаниеЕ", max_length=250)

    class Meta:
        verbose_name = "НомеР отеля"
        verbose_name_plural = "НомерА отелЯ"

    def __str__(self):
        return self.title


class HotelFields(models.Model):
    """"Поля отеля"""
    title = models.CharField("НазваниЕ", max_length=250)
    sub_title = models.CharField("ОписаниеЕ", max_length=250, default="")
    icon = models.CharField("ИконкА", max_length=250, default="")
    about_room = models.ForeignKey(
        HotelRooms,
        verbose_name='О номерЕ',
        on_delete=models.CASCADE,
        related_name='about_rooM'
    )

    class Meta:
        verbose_name = "Поле НомероВ"
        verbose_name_plural = "Поля НомероВ"

    def __str__(self):
        return self.title


class RatingRooms(models.Model):
    """"Оценка сервисов номеров"""
    title = models.CharField("НазваНие", max_length=250)
    rating = models.FloatField("Оценка", validators=[MinValueValidator(1), MaxValueValidator(10)], default="")
    services = models.ForeignKey(
        HotelRooms,
        verbose_name='Оценка сервиса номеров',
        on_delete=models.CASCADE,
        related_name='services'
    )

    class Meta:
        verbose_name = "Оценка сервисА НомероВ"
        verbose_name_plural = "Оценки сервисОВ НомероВ"

    def __str__(self):
        return self.title


class BookingRoom(models.Model):
    """"Модель бронирования номеров"""

    entry_date = models.CharField("Дата заезда", max_length=100)
    depart_date = models.CharField("Дата выезда", max_length=100)
    name = models.CharField("ИмЯ", max_length=100)
    phone = models.CharField("Телефон", max_length=100)
    comment = models.TextField("Комментрарий", max_length=1000, blank=True)
    adult = models.PositiveIntegerField("ВзрослыЕ", default=0)
    children = models.PositiveIntegerField("ДетИ", default=0)
    rooms = models.ForeignKey(
        HotelRooms,
        verbose_name='Заказной номер',
        on_delete=models.CASCADE,

    )

    class Meta:
        verbose_name = "Забранированный НомеР"
        verbose_name_plural = "Забранированные НомеРА"

    def __str__(self):
        return self.name
