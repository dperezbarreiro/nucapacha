from django.db import models
from ckeditor.fields import RichTextField


class SpecialOffer(models.Model):

    title = models.CharField(max_length=35)
    text = RichTextField(max_length=100)
    code = models.CharField(max_length=6)

    title_es = models.CharField(max_length=35, verbose_name="Titulo")
    text_es = RichTextField(max_length=100, verbose_name="Texto")
    code_es = models.CharField(max_length=6, verbose_name="Codigo")

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Special Offer'
        verbose_name_plural = 'Special Offers'
