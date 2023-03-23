from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from django.utils.crypto import get_random_string
from django.db.models.signals import pre_save

from config.utils import unique_slug_generator
from baseapp.models import BaseModel


class EventType(BaseModel):
    title = models.CharField(max_length=256, verbose_name='Номи')

    class Meta:
        db_table = 'event_type'
        verbose_name = 'Тадбир тури'
        verbose_name_plural = 'Тадбир турлари'
        ordering = ['title']

    def __str__(self):
        return self.title


class Event(BaseModel):
    title = models.CharField(max_length=255, verbose_name='Мавзу')
    content = models.TextField(verbose_name='Матн')
    photo = models.ImageField(upload_to='events', verbose_name="Асосий расм")
    thumbnail = ImageSpecField(source='photo',
                               processors=[ResizeToFit(370)],
                               options={'quality':100})
    capture = ImageSpecField(source='photo',
                             processors=[ResizeToFit(30)],
                             options={'quality': 60})
    start_time = models.DateTimeField(verbose_name='Бошланиш вақти')
    end_time = models.DateTimeField(verbose_name='Тугаш вақти')
    responsible_org = models.CharField(max_length=255, verbose_name="Масъул ташкилот")
    pub_date = models.DateField(verbose_name="Эълон Санаси", blank=True, null=True)
    views = models.IntegerField(default=0, verbose_name="Кўришлар сони")
    on_slider = models.BooleanField(default=False)
    num_visitors = models.IntegerField(default=0, verbose_name='Ташриф буюрувчилар сони')
    is_active = models.BooleanField(default=False, verbose_name='Актив')
    type = models.ForeignKey(EventType, related_name='types', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'event'
        verbose_name = 'Тадбир'
        verbose_name_plural = 'Тадбирлар'
        ordering = ['-start_time']

    def __str__(self):
        return self.title


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        title = ''
        if instance.title_uz is not None and instance.title_uz != '':
            title = instance.title_uz
        elif instance.title_uzb is not None and instance.title_uzb != '':
            title = instance.title_uzb
        elif instance.title_ru is not None and instance.title_ru != '':
            title = instance.title_ru
        elif instance.title_en is not None and instance.title_en != '':
            title = instance.title_en
        else:
            title = get_random_string(8, '0123456789')

        instance.slug = unique_slug_generator(instance, title=title)


pre_save.connect(slug_generator, sender=Event)
pre_save.connect(slug_generator, sender=EventType)


class EventImages(models.Model):
    event = models.ForeignKey(
        Event, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='EventImages', blank=True, null=True, verbose_name="Расм")
    thumbnail = ImageSpecField(source='image',
                               processors=[ResizeToFit(height=700)],
                               options={'quality': 100})
    capture = ImageSpecField(source="image",
                             processors=[ResizeToFit(30)],
                             options={'quality': 60})

    class Meta:
        db_table = 'event_images'
        verbose_name = 'Тадбир Расм'
        verbose_name_plural = 'Тадбир Расмлар'

    def __str__(self):
        return f"{self.event.title}'s images"
