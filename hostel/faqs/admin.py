from django.contrib import admin
from bulk_admin import BulkModelAdmin
from .models import Faq


@admin.register(Faq)
class FaqAdmin(BulkModelAdmin):
        model = Faq