from django.db import models
from ckeditor.fields import RichTextField


class RoomsDescription(models.Model):

    title = models.CharField(max_length=25)
    text = RichTextField()

    title_es = models.CharField(max_length=25, verbose_name="Titulo")
    text_es = RichTextField(verbose_name="Texto")

    def __str__(self):
        return 'Rooms'

    class Meta:
        verbose_name = 'Rooms description'
        verbose_name_plural = 'Rooms description'


class Room(models.Model):

    room = models.CharField(max_length=40)
    price_shared = models.FloatField()
    price_private = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.room

    class Meta:
        verbose_name = 'Room & Price'
        verbose_name_plural = 'Rooms & Prices'

