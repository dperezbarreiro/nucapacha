from django.db import models
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe


class ActivitiesDescription(models.Model):

    title = models.CharField(max_length=25)
    text = RichTextField()

    title_es = models.CharField(max_length=25, verbose_name="Titulo")
    text_es = RichTextField(verbose_name="Texto")

    def __str__(self):
        return "Activities"

    class Meta:
        verbose_name = 'Activities description'
        verbose_name_plural = 'Activities description'


class Activity(models.Model):

    image = models.ImageField()

    title = models.CharField(max_length=25)
    text = RichTextField()

    title_es = models.CharField(max_length=25, verbose_name="Titulo")
    text_es = RichTextField(verbose_name="Texto")

    url = models.URLField()

    def __str__(self):
        return "Activity"

    def image_tag(self):
        return mark_safe('<img src="/uploads/%s" height="50"/>' % self.image)

    image_tag.short_description = 'Image'

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'


class Event(models.Model):

    image = models.ImageField()

    title = models.CharField(max_length=25)
    text = RichTextField()

    title_es = models.CharField(max_length=25, verbose_name="Titulo")
    text_es = RichTextField(verbose_name="Texto")

    url = models.URLField()

    def __str__(self):
        return "Event"

    def image_tag(self):
        return mark_safe('<img src="/uploads/%s" height="50"/>' % self.image)

    image_tag.short_description = 'Image'

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
