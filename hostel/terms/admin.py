from django.contrib import admin
from .models import Terms


@admin.register(Terms)
class TermsAdmin(admin.ModelAdmin):
        model = Terms

        def has_add_permission(self, request):
                return False

        def has_delete_permission(self, request, obj=None):
                return False
