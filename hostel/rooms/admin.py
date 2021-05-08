from django.contrib import admin
from .models import Room, RoomsDescription


@admin.register(RoomsDescription)
class RoomsDescriptionAdmin(admin.ModelAdmin):
    model = RoomsDescription
    list_display = ('title', 'text',)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    model = Room
    readonly_fields = ('room',)
    list_display = ('room', 'price_shared')
    fields = ('room', 'price_shared', 'price_private')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
