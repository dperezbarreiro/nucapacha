from django.contrib import admin
from .models import AboutUs


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
        model = AboutUs
        list_display = ('title', 'text',)

        def has_add_permission(self, request):
                return False

        def has_delete_permission(self, request, obj=None):
                return False
