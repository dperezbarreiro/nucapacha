from django.db import models
from ckeditor.fields import RichTextField


class AboutUs(models.Model):

    title = models.CharField(max_length=25)
    text = RichTextField()

    title_es = models.CharField(max_length=25, verbose_name="Titulo")
    text_es = RichTextField(verbose_name="Texto")

    video_URL = models.URLField()

    def __str__(self):
        return "About Us"

    class Meta:
        verbose_name = 'About Us description'
        verbose_name_plural = 'About Us description'
