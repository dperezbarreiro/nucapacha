from django.db import models
from ckeditor.fields import RichTextField


class Location(models.Model):

    title = models.CharField(max_length=25)
    text = RichTextField()

    title_es = models.CharField(max_length=25, verbose_name="Titulo")
    text_es = RichTextField(verbose_name="Texto")

    def __str__(self):
        return "Location"

    class Meta:
        verbose_name = 'Location description'
        verbose_name_plural = 'Location description'


