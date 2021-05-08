from django.contrib import admin
from .models import CarouselImage


@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
        model = CarouselImage

        list_display = ('image_tag', 'title', 'subtitle')

