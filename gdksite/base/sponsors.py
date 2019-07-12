from gdksite.base.models import Sponsor
from gdksite.event.models import EventSponsorRelationship, EventPage


from django.views import View
from django.views.generic import TemplateView
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse



class SponsorsView(TemplateView):

    template_name = 'sponsors.html'
    success_url = None

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['sponsors'] = []
        for s in Sponsor.objects.all():
            #img = generate_image_url(s.image, 'fill-457x480-c0')
            #print(img)
            event_pages = EventSponsorRelationship.objects.filter(sponsors_id=s.id).values_list('page_id', flat=True)
            events = EventPage.objects.filter(id__in=event_pages)
            context['events'] = events
            context['sponsors'].append({
            'name': s.name,
            'address': s.adress,
            'link' : s.link,
            'image': s.image,
            'category' : s.category,
            'description' : s.description,
            'events': events
            })
        print(context['sponsors'])

        return context
