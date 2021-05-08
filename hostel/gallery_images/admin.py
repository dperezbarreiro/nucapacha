from django.contrib import admin
from .models import GalleryImage


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
        model = GalleryImage

        list_display = ('image_tag', 'category',)

