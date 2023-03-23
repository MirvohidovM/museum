from django.db import models
from django.db.models.signals import pre_save
from django.utils.crypto import get_random_string
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

from baseapp.models import BaseModel
from config.utils import compressImage, unique_slug_generator


class PhotoGallery(BaseModel):
    title = models.CharField(max_length=500, verbose_name="Галерея номи")
    photo = models.ImageField(upload_to='images', verbose_name="Асосий расм")
    thumbnail = ImageSpecField(source='photo',
                               processors=[ResizeToFit(400)],
                               options={'quality': 100})
    capture = ImageSpecField(source='photo',
                               processors=[ResizeToFit(30)],
                               options={'quality': 60})
    class Meta:
        db_table = 'photo_gallery'
        verbose_name = "Фото галерея"
        verbose_name_plural = "Фото галерея"
        ordering = ['title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(PhotoGallery, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.photo:
            self.photo.delete()
        if self.images:
            for image in self.images.all():
                image.delete()
        super(PhotoGallery, self).delete(*args, **kwargs)


class PhotoGalleryImages(models.Model):
    gallery = models.ForeignKey(
        PhotoGallery, related_name='images', on_delete=models.CASCADE, verbose_name="Тасвирлар")
    image = models.ImageField(
        upload_to='PhotoGallery/', blank=True, null=True, verbose_name="Расм")
    # thumbnail = ImageSpecField(source="image",
    #                          processors=[ResizeToFit(490)],
    #                          options={'quality': 100})
    # capture = ImageSpecField(source="image",
    #                          processors=[ResizeToFit(30)],
    #                          options={'quality': 60})

    class Meta:
        db_table = 'photo_gallery_images'

    def save(self, *args, **kwargs):
        if self.image:
            self.image = compressImage(self.image)
        super(PhotoGalleryImages, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete()
        super(PhotoGalleryImages, self).save(*args, **kwargs)


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        title = ''
        if instance.title_uz is not None and instance.title_uz != "":
            title = instance.title_uz
        elif instance.title_ru is not None and instance.title_ru != "":
            title = instance.title_ru
        elif instance.title_uzb is not None and instance.title_uzb != "":
            title = instance.title_uzb
        elif instance.title_en is not None and instance.title_en != "":
            title = instance.title_en
        else:
            title = get_random_string(8, '0123456789')
        instance.slug = unique_slug_generator(instance, title)


pre_save.connect(slug_generator, sender=PhotoGallery)
