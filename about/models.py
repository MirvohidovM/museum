from django.db import models
from solo.models import SingletonModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit


class About(SingletonModel):
    id = models.IntegerField(primary_key=True, editable=False)
    description = models.TextField(
        blank=True, null=True, verbose_name="Биз ҳақимизда")
    on_slider = models.BooleanField(default=False)

    class Meta:
        db_table = 'about'
        verbose_name = "Музей тарихи"
        verbose_name_plural = "Музей тарихи"

    def __str__(self):
        return 'Музей тарихи'


class AboutImages(models.Model):
    about = models.ForeignKey(About, related_name='images', on_delete=models.CASCADE,
                              verbose_name='Расмлар')
    image = models.ImageField(upload_to='AboutImages', blank=True,
                              verbose_name='Фото')
    thumbnail = ImageSpecField(source='image', processors=[ResizeToFit(883)],
                             options={'quality': 80})
    capture = ImageSpecField(source='image', processors=[ResizeToFit(30)],
                             options={'quality': 60})
    class Meta:
        db_table = 'about_images'
