from django.views.generic import ListView
from .models import AboutUs
from hostel.rooms.models import Room
from hostel.services.models import Service


class AboutUsList(ListView):
    model = AboutUs
    context_object_name = 'about_us'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['rooms'] = Room.objects.all()
        context['services'] = Service.objects.all()
        return context
