from modeltranslation.translator import register, TranslationOptions

from about.models import About
from exhibit.models import Exhibit, Category
from gallery.models import PhotoGallery
from employee.models import Employee
from useful_link.models import UsefulLink
from news.models import News
from event.models import Event, EventType
from order.models import Order, ExcursionType
from karusel.models import Karusel
from contact.models import Contact, LandmarkPhotos


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('description',)
    required_languages = ('uz',)


@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('address', 'transport',)


@register(LandmarkPhotos)
class LandmarkPhotosTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Employee)
class EmployeeTranslationOptions(TranslationOptions):
    fields = ('name', 'position')
    required_languages = {'uz': ('name',)}


@register(UsefulLink)
class UsefulLinkTranslationOptions(TranslationOptions):
    fields = ['title']


@register(PhotoGallery)
class PhotoGalleryTranslationOptions(TranslationOptions):
    fields = ['title']


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)
    required_languages = {'uz': ('title', 'content')}


@register(Event)
class MenuTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'responsible_org',)
    required_languages = ('uz',)


@register(EventType)
class EventTypeTranslationOptions(TranslationOptions):
    fields = ('title',)
    required_languages = ('uz',)


@register(Order)
class OrderTranslationOptions(TranslationOptions):
    fields = ['firstname', 'lastname', 'organization']
    # required_languages = ('uz',)


@register(ExcursionType)
class ExcursionTypeTranslationOptions(TranslationOptions):
    fields = ['name']
    # required_languages = ('uz',)


@register(Category)
class ExhibitCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
    required_languages = ('uz',)


@register(Exhibit)
class ExhibitTranslationOptions(TranslationOptions):
    fields = ('name', 'summary', 'used_years', 'body', 'audio')
    required_languages = {'uz': ('name', 'summary', 'used_years', 'body',)}


@register(Karusel)
class KaruselTranslationOptions(TranslationOptions):
    fields = ('title',)
    required_languages = ('uz',)
