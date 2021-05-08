from ckeditor.fields import RichTextField
from django.db import models


class Popup(models.Model):
    DISPLAY_OPTIONS = (
        ('once', 'Once'),
        ('daily', 'Daily'),
        ('always', 'Always'),
    )

    reference = models.CharField(max_length=1024)
    html = RichTextField()
    html_es = RichTextField()
    visible_from = models.DateTimeField(blank=True, null=True)
    visible_until = models.DateTimeField(blank=True, null=True)
    display_options = models.CharField(max_length=255, choices=DISPLAY_OPTIONS, default='daily')
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Popups"

    class Meta:
        verbose_name = 'Popup'
        verbose_name_plural = 'Popups'
