from django.db import models
from django_countries.fields import CountryField
from core.models import TimeStampedModel


class AbstractItem(TimeStampedModel):

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    pass


class Room(TimeStampedModel):

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    badrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room_type = models.ManyToManyField("rooms.RoomType", blank=True)

    def __str__(self):
        return self.name
