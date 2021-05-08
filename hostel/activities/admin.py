from django.contrib import admin
from .models import ActivitiesDescription, Activity, Event


@admin.register(ActivitiesDescription)
class ActivitiesDescriptionAdmin(admin.ModelAdmin):
        model = ActivitiesDescription
        list_display = ('title', 'text',)

        def has_add_permission(self, request):
                return False

        def has_delete_permission(self, request, obj=None):
            return False


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
        model = Activity
        list_display = ('title', 'text', 'image_tag',)


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
        model = Event
        list_display = ('title', 'text', 'image_tag',)
