from django.contrib import admin
from .models import Location


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
        model = Location
        list_display = ('title', 'text',)

        def has_add_permission(self, request):
                return False

        def has_delete_permission(self, request, obj=None):
            return False


