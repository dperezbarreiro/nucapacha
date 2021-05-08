from django.contrib import admin
from .models import Facility


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
        model = Facility
        list_display = ('title', 'text',)

        def has_add_permission(self, request):
                return False

        def has_delete_permission(self, request, obj=None):
                return False
