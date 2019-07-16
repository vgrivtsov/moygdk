from __future__ import unicode_literals

from django.contrib import messages
from django.db import models
from django.shortcuts import redirect, render
from django.core.validators import( MaxValueValidator,
    MinValueValidator, validate_comma_separated_integer_list)

from modelcluster.contrib.taggit import ClusterTaggableManager
from modelcluster.fields import ParentalKey

from taggit.models import Tag, TaggedItemBase

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.core.blocks import IntegerBlock, DateTimeBlock

from gdksite.base.blocks import BaseStreamBlock

from datetime import datetime

class EventPageTag(TaggedItemBase):
    """
    This model allows us to create a many-to-many relationship between
    the EventPage object and tags. There's a longer guide on using it at
    http://docs.wagtail.io/en/latest/reference/pages/model_recipes.html#tagging
    """
    content_object = ParentalKey('EventPage', related_name='tagged_items', on_delete=models.CASCADE)


class EventSponsorRelationship(Orderable, models.Model):
    """
    This defines the relationship between the `Sponsor` within the `base`
    app and the EventPage below. This allows Sponsor to be added to a EventPage.

    We have created a two way relationship between EventPage and Sponsor using
    the ParentalKey and ForeignKey
    """
    page = ParentalKey(
        'EventPage', related_name='event_sponsor_relationship', on_delete=models.CASCADE
    )
    sponsors = models.ForeignKey(
        'base.Sponsor', related_name='sponsor_event_relationship', on_delete=models.CASCADE
    )
    panels = [
        SnippetChooserPanel('sponsors')
    ]


class EventPage(Page):
    """
    A Event Page

    We access the People object with an inline panel that references the
    ParentalKey's related_name in EventPeopleRelationship. More docs:
    http://docs.wagtail.io/en/latest/topics/pages.html#inline-models
    """
    introduction = models.TextField(
        help_text='Text to describe the page',
        verbose_name="Место проведения",
        blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.',
        verbose_name="Картинка",
    )
    body = StreamField(
        BaseStreamBlock(), verbose_name="Основное описание",
                           blank=True, null=True
    )
    subtitle = models.CharField(blank=True, max_length=255, verbose_name="Краткое описание")
    tags = ClusterTaggableManager(through=EventPageTag, blank=True)
    age_policy = models.PositiveIntegerField(verbose_name="Возрастное ограничение",
                                             default=3,
                                             validators=[
                                                     MaxValueValidator(18),
                                                     MinValueValidator(0)
                                                     ]
    )
    event_date = models.DateField(auto_now_add=False, null=True, verbose_name="Дата проведения мероприятия")
    event_time = models.TimeField(auto_now_add=False, null=True, verbose_name="Время проведения мероприятия")

    content_panels = Page.content_panels + [
        FieldPanel('subtitle', classname="full"),
        FieldPanel('introduction', classname="full"),
        ImageChooserPanel('image'),
        StreamFieldPanel('body'),
        FieldPanel('event_date'),
        FieldPanel('event_time'),
        FieldPanel('age_policy'),
        InlinePanel(
            'event_sponsor_relationship', label="Спонсор(ы)",
            panels=None),
        FieldPanel('tags'),
    ]

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    def sponsors(self):

        sponsors = [
            n.sponsors for n in self.event_sponsor_relationship.all()
        ]

        return sponsors

    @property
    def get_tags(self):
        """
        Similar to the authors function above we're returning all the tags that
        are related to the Event post into a list we can access on the template.
        We're additionally adding a URL to access EventPage objects with that tag
        """
        tags = self.tags.all()
        for tag in tags:
            tag.url = '/'+'/'.join(s.strip('/') for s in [
                self.get_parent().url,
                'tags',
                tag.slug
            ])
        return tags

    # Specifies parent to EventPage as being EventIndexPages
    parent_page_types = ['EventIndexPage']

    # Specifies what content types can exist as children of EventPage.
    # Empty list means that no child content types are allowed.
    subpage_types = []


class EventIndexPage(RoutablePageMixin, Page):
    """
    Index page for Events.
    We need to alter the page model's context to return the child page objects,
    the EventPage objects, so that it works as an index page

    RoutablePageMixin is used to allow for a custom sub-URL for the tag views
    defined above.
    """
    introduction = models.TextField(
        help_text='Text to describe the page',
        blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
    )

    content_panels = Page.content_panels + [
        FieldPanel('introduction', classname="full"),
        ImageChooserPanel('image'),
    ]

    # Speficies that only EventPage objects can live under this index page
    subpage_types = ['EventPage']

    # Defines a method to access the children of the page (e.g. EventPage
    # objects). On the demo site we use this on the HomePage
    def children(self):
        return self.get_children().specific().live()

    # Overrides the context to list all child items, that are live, by the
    # date that they were published
    # http://docs.wagtail.io/en/latest/getting_started/tutorial.html#overriding-context
    def get_context(self, request):
        context = super(EventIndexPage, self).get_context(request)
        context['events'] = EventPage.objects.descendant_of(
            self).live().order_by(
            'event_date')
        context['nowtime'] = datetime.now().date()

        return context

    # This defines a Custom view that utilizes Tags. This view will return all
    # related EventPages for a given Tag or redirect back to the EventIndexPage.
    # More information on RoutablePages is at
    # http://docs.wagtail.io/en/latest/reference/contrib/routablepage.html
    @route('^tags/$', name='tag_archive')
    @route('^tags/([\w-]+)/$', name='tag_archive')
    def tag_archive(self, request, tag=None):

        try:
            tag = Tag.objects.get(slug=tag)
        except Tag.DoesNotExist:
            if tag:
                msg = 'There are no Event events tagged with "{}"'.format(tag)
                messages.add_message(request, messages.INFO, msg)
            return redirect(self.url)

        events = self.get_events(tag=tag)

        context = {
            'tag': tag,
            'events': events,
            'nowtime': datetime.now().date()
        }

        return render(request, 'event/event_index_page.html', context)

    def serve_preview(self, request, mode_name):
        # Needed for previews to work
        return self.serve(request)

    # Returns the child EventPage objects for this EventPageIndex.
    # If a tag is used then it will filter the events by tag.
    def get_events(self, tag=None):
        events = EventPage.objects.live().descendant_of(self)
        if tag:
            events = events.filter(tags=tag)
        return events

    # Returns the list of Tags for all child events of this EventPage.
    def get_child_tags(self):
        tags = []
        for post in self.get_events():
            # Not tags.append() because we don't want a list of lists
            tags += post.get_tags
        tags = sorted(set(tags))
        return tags
