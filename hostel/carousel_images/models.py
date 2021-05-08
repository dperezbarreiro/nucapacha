from django.db import models
from django.utils.safestring import mark_safe


class CarouselImage(models.Model):

    image = models.ImageField()
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=50)

    title_es = models.CharField(max_length=30)
    subtitle_es = models.CharField(max_length=50)

    def image_tag(self):
        return mark_safe('<img src="/uploads/%s" height="50"/>' % self.image)

    image_tag.short_description = 'Image'