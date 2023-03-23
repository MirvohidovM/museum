from django.db import models
from solo.models import SingletonModel

from config.utils import (imagefile_validation_exception,
                          unique_slug_generator,)


class Karusel(SingletonModel):
    title = models.TextField(verbose_name='Мавзу')

    class Meta:
        db_table = 'karusel'
        verbose_name = 'Бош саҳифа мавзуси'
        verbose_name_plural = 'Бош саҳифа мавзуси'

    def __str__(self):
        return self.title


class KaruselImages(models.Model):
    karusel = models.ForeignKey(Karusel, related_name='images', on_delete=models.CASCADE)
    image = models.FileField(upload_to='KoruselImages', verbose_name='Расмлар',
                             blank=True, null=True, validators=[imagefile_validation_exception])

    class Meta:
        db_table = 'karusel_images'
        verbose_name = 'Карусел расми'
        verbose_name_plural = 'Карусел расмлари'

    def __str__(self):
        return f"{self.karusel.title} расмлари"
