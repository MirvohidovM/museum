from django.db import models
from django.db.models.signals import pre_save
from django.utils.crypto import get_random_string

from baseapp.models import BaseModel
from config.utils import random_string_generator, unique_slug_generator
from config.validation import file_validation_exception
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


class UsefulLink(BaseModel):
    title = models.CharField(max_length=256, blank=True, null=True, verbose_name="Сарлавҳа")
    link = models.URLField(max_length=500, null=True, blank=True, verbose_name="Ҳавола")
    image = models.FileField(upload_to="images/usefullink", blank=True, null=True,
                             verbose_name="Расм", validators=[file_validation_exception])
    index = models.IntegerField(null=True, blank=True, verbose_name='Индекс')

    class Meta:
        db_table = "useful_link"
        verbose_name = "Фойдали ҳавола"
        verbose_name_plural = "Фойдали ҳаволалар"
        ordering = ['index']

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        return super(UsefulLink, self).delete(*args, **kwargs)


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


pre_save.connect(slug_generator, sender=UsefulLink)
