from django.db import models
from ckeditor.fields import RichTextField


class Terms(models.Model):

    title = models.CharField(max_length=120)
    text = RichTextField()

    title_es = models.CharField(max_length=120, verbose_name='Titulo')
    text_es = RichTextField(verbose_name='Texto')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Terms & Conditions'
        verbose_name_plural = 'Terms & Conditions'