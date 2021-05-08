from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.db.models import Q
from django.utils import timezone

from hostel.about_us.models import AboutUs
from hostel.activities.models import ActivitiesDescription, Activity, Event
from hostel.carousel_images.models import CarouselImage
from hostel.facilities.models import Facility
from hostel.faqs.models import Faq
from hostel.gallery_images.models import GalleryImage
from hostel.location.models import Location
from hostel.rooms.models import Room, RoomsDescription
from hostel.special_offers.models import SpecialOffer
from hostel.terms.models import Terms
from hostel.popups.models import Popup
from .forms import ContactForm


class EventView(TemplateView):
    template_name = "events.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['lang'] = self.request.session['lang'].strip() if 'lang' in self.request.session else 'en'
        context['terms'] = Terms.objects.all().first()
        context['faqs'] = Faq.objects.all()
        context['special_offer'] = SpecialOffer.objects.all().first()
        context['events'] = Event.objects.all()
        return context


class HostelView(FormView):
    template_name = "index.html"
    form_class = ContactForm
    success_url = '/'

    def __init__(self, *args, **kwargs):
        super(HostelView, self).__init__(*args, **kwargs)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        if 'lang' in self.request.session:
            if self.request.session['lang'] == 'es':
                context['form'].fields['name'].label = 'Nombre'
                context['form'].fields['mail'].label = 'Correo electronico'
                context['form'].fields['message'].label = 'Mensaje'
        context['lang'] = self.request.session['lang'].strip() if 'lang' in self.request.session else 'en'
        context['about_us'] = AboutUs.objects.all().first()
        context['location'] = Location.objects.all().first()
        context['rooms'] = Room.objects.all()
        context['rooms_description'] = RoomsDescription.objects.all().first()
        context['facilities'] = Facility.objects.all().first()
        context['activities'] = ActivitiesDescription.objects.all().first()
        context['events'] = Activity.objects.all()
        context['gallery_images'] = GalleryImage.objects.all()
        context['carousel_images'] = CarouselImage.objects.all()
        context['terms'] = Terms.objects.all().first()
        context['faqs'] = Faq.objects.all()
        context['special_offer'] = SpecialOffer.objects.all().first()

        # Popups
        now = timezone.now()

        context['popup'] = Popup.objects.filter(
            enabled=True
        ).filter(
            Q(visible_from__isnull=True) | Q(visible_from__lte=now)
        ).filter(
            Q(visible_until__isnull=True) | Q(visible_until__gte=now)
        ).order_by(
            'visible_until'
        ).first()

        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return HttpResponse("Message sent! Thank you.")


def switch_lang(request, lang):
    request.session['lang'] = lang
    return HttpResponse()
