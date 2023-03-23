from baseapp.models import BaseModel
from django.db import models
from django.db.models.signals import pre_save
from django.utils.crypto import get_random_string
from config.utils import unique_slug_generator, compressImage
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from django.utils.timezone import now


class News(BaseModel):
    title = models.CharField(max_length=500, verbose_name="Сарлавҳа")
    content = models.TextField(null=True, blank=True, verbose_name="Матни")
    photo = models.ImageField(upload_to='news', verbose_name="Асосий расм")
    thumbnail = ImageSpecField(source='photo',
                               processors=[ResizeToFit(360)],
                               options={'quality':60})
    capture = ImageSpecField(source='photo',
                             processors=[ResizeToFit(30)],
                             options={'quality': 60})
    views = models.IntegerField(default=0, blank=True, null=True,
                                verbose_name="Кўришлар Сони")
    pub_date = models.DateField(default=now, verbose_name="Санаси")
    on_slider = models.BooleanField(default=False)

    class Meta:
        db_table = "news"
        verbose_name = 'Янгилик'
        verbose_name_plural = 'Янгиликлар'
        ordering = ['-pub_date', '-created_at']

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


pre_save.connect(slug_generator, sender=News)


class NewsImages(models.Model):
    news = models.ForeignKey(News, related_name='images', on_delete=models.CASCADE,
                             verbose_name="Расмлар")
    image = models.ImageField(upload_to='NewsImages',
                              blank=True, null=True, verbose_name=('Фото'))
    thumbnail = ImageSpecField(source='image',
                               processors=[ResizeToFit(height=700)],
                               options={'quality': 100})
    capture = ImageSpecField(source='image',
                             processors=[ResizeToFit(30)],
                             options={'quality': 60})
    is_active = models.BooleanField(default=True, verbose_name='Актив')
    index = models.IntegerField(
        null=True, blank=True, verbose_name="Тартиб рақами")

    class Meta:
        db_table = "news_images"
        ordering = ['index']

    def save(self, *args, **kwargs):
        if self.image:
            self.image = compressImage(self.image)
        super(NewsImages, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        super(NewsImages, self).delete(*args, **kwargs)
