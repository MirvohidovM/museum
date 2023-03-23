from django.db import models
from django.db.models.signals import pre_save
from django.utils.crypto import get_random_string
from imagekit.models.fields import ImageSpecField
from pilkit.processors.resize import ResizeToFit

from baseapp.models import BaseModel
from config.utils import validate_file_extension, unique_slug_generator
from config.validation import file_validation_exception


class Category(BaseModel):
    name = models.CharField("Номи:", max_length=200)
    logo = models.FileField("Логотип: ", upload_to='exhibit/logos/', null=True, blank=True,
                            validators=[file_validation_exception])
    index = models.PositiveSmallIntegerField(default=0, verbose_name='Тартиб рақами')
    to_main_page = models.BooleanField(default=False, verbose_name='Бош саҳифа')

    class Meta:
        ordering = ('index', )
        db_table = "exhibit_category"
        verbose_name = "Категория"
        verbose_name_plural = "Категориялар"

    def __str__(self):
        return self.name


class Exhibit(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="Категория",
                                 related_name='categories')
    name = models.CharField("Номи: ", max_length=255)
    summary = models.TextField("Қисқача: ", max_length=2500)
    body = models.TextField("Экспонат ҳақида: ")
    used_years = models.CharField("Фойдаланилган даври: ", max_length=100)
    invented_year = models.CharField("Ихтиро йили: ", max_length=4)
    audio = models.FileField("Аудио: ", validators=[validate_file_extension], upload_to='exhibit/audios/', blank=True)
    cover = models.ImageField("Расм", upload_to='exhibit/images/')
    thumbnail = ImageSpecField(source='cover',
                               processors=[ResizeToFit(370)],
                               options={'quality': 100})
    capture = ImageSpecField(source='cover',
                             processors=[ResizeToFit(30)],
                             options={'quality': 60})
    gif = models.ImageField(upload_to='exhibit/gifs/', blank=True, null=True,
                            verbose_name='Gif')
    to_main_page = models.BooleanField(default=False, verbose_name='Бош саҳифа')
    to_about_page = models.BooleanField(default=False, verbose_name='Музей ҳақида')

    class Meta:
        ordering = ('invented_year',)
        db_table = "exhibit"
        verbose_name = "Экспонат"
        verbose_name_plural = "Экспонатлар"

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        if self.cover:
            self.cover.delete()
        if self.audio:
            self.audio.delete()
        if self.images:
            for image in self.images.all():
                image.delete()
        return super(Exhibit, self).delete(*args, **kwargs)


class ExhibitImages(models.Model):
    exhibit = models.ForeignKey(Exhibit, on_delete=models.CASCADE, verbose_name="Экспонат: ", related_name="images")
    image = models.ImageField('Расм: ', upload_to='exhibit/images/')
    thumbnail = ImageSpecField(source='image',
                               processors=[ResizeToFit(370)],
                               options={'quality': 100})
    capture = ImageSpecField(source='image',
                             processors=[ResizeToFit(30)],
                             options={'quality': 60})

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        return super(ExhibitImages, self).delete(*args, **kwargs)

    class Meta:
        db_table = "exhibit_images"
        verbose_name = "Расм"
        verbose_name_plural = "Расмлар"


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        name = ''
        if instance.name_uz is not None and instance.name_uz != '':
            name = instance.name_uz
        elif instance.name_uzb is not None and instance.name_uzb != '':
            name = instance.name_uzb
        elif instance.name_ru is not None and instance.name_ru != '':
            name = instance.name_ru
        elif instance.name_en is not None and instance.name_en != '':
            name = instance.name_en
        else:
            name = get_random_string(8, '0123456789')
        instance.slug = unique_slug_generator(instance, title=name)


pre_save.connect(slug_generator, sender=Category)
pre_save.connect(slug_generator, sender=Exhibit)
