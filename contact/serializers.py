from rest_framework import serializers
from django.core.files.images import get_image_dimensions
from django.conf import settings

from .models import Contact, LandmarkPhotos


class LandmarkPhotosSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField('get_thumbnail')

    class Meta:
        model = LandmarkPhotos
        fields = ['name', 'thumbnail']

    def get_thumbnail(self, obj):
        if obj.thumbnail:
            img_url = obj.thumbnail.url
            path = '{domain}{path}'.format(domain=settings.BACK_URL, path=img_url)
            try:
                w, h = get_image_dimensions(obj.thumbnail.file)
                data = {
                    'src': path,
                    'weight': w,
                    'height': h,
                }
                return data
            except Exception:
                return None
        else:
            return None


class ContactSerializer(serializers.ModelSerializer):
    landmarks = LandmarkPhotosSerializer(many=True)

    class Meta:
        model = Contact
        fields = ['address', 'transport', 'phone', 'email', 'landmarks']