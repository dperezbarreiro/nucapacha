from bulk_admin import BulkModelAdmin
from django.contrib import admin
from .models import Popup


@admin.register(Popup)
class PopupAdmin(BulkModelAdmin):
    model = Popup
