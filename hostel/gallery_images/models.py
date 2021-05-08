from django.db import models
from django.utils.safestring import mark_safe


class GalleryImage(models.Model):

    IMAGE_CATEGORIES = (
        ('pool-bar', 'Pool&Bar'),
        ('breakfast', 'Breakfast'),
        ('tv', 'TV Room'),
        ('rooms', 'Guest Rooms'),
    )

    image = models.ImageField()
    category = models.CharField(max_length=10, choices=IMAGE_CATEGORIES)

    def image_tag(self):
        return mark_safe('<img src="/uploads/%s" height="50"/>' % self.image)

    image_tag.short_description = 'Image'

