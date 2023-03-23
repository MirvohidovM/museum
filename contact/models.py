from django.db import models
from solo.models import SingletonModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


class Contact(SingletonModel):
    address = models.CharField(max_length=255, verbose_name='Манзил')
    transport = models.TextField(max_length=255, verbose_name='Транспорт')
    phone = models.TextField(verbose_name='Телефон')
    email = models.TextField(verbose_name='Email почта')

    class Meta:
        db_table = 'contact'
        verbose_name = "Боғланиш"
        verbose_name_plural = "Боғланиш"


class LandmarkPhotos(models.Model):
    name = models.CharField(default='', max_length=255, verbose_name="Мўлжал")
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='landmarks')
    photo = models.ImageField(upload_to='ContactPhotos', verbose_name='Расм')
    thumbnail = ImageSpecField(source='photo',
                               processors=[ResizeToFit(370)],
                               options={'quality': 70})

    class Meta:
        db_table = 'landmark_photos'
        verbose_name = "Мўлжал расми"
        verbose_name_plural = "Мўлжал расмлари"
        ordering = ('id',)