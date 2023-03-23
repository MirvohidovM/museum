from django.db import models
from django.db.models.signals import pre_save
from django.utils.crypto import get_random_string
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

from config.utils import compressImage, unique_slug_generator
from baseapp.models import BaseModel


class Employee(BaseModel):
    name = models.CharField(max_length=500, verbose_name="Тўлиқ Исм")
    position = models.CharField(max_length=500, verbose_name='Лавозим')
    phone = models.CharField(max_length=30, verbose_name='Телефон рақам')
    email = models.EmailField(max_length=254, verbose_name='Электрон почта')
    photo = models.ImageField(upload_to='EmployeeImages', blank=True, null=True, verbose_name='Расм')
    thumbnail_240 = ImageSpecField(source='photo',
                               processors=[ResizeToFit(400)],
                               options={'quality': 100})
    thumbnail_160 = ImageSpecField(source='photo',
                             processors=[ResizeToFit(160)],
                             options={'quality': 60})
    is_lidership = models.BooleanField(default=False, verbose_name='Раҳбарият')
    index = models.IntegerField(blank=True, null=True, verbose_name='Тартиб рақами')

    class Meta:
        db_table = "employee"
        verbose_name = 'Ходим'
        verbose_name_plural = 'Ходимлар'
        ordering = ['index']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.photo:
            self.photo = compressImage(self.photo)
        super(Employee, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.photo:
            self.photo.delete()
        super(Employee, self).delete(*args, **kwargs)


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


pre_save.connect(slug_generator, sender=Employee)
