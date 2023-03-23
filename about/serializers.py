import base64
from rest_framework import serializers
from django.core.files.images import get_image_dimensions
from django.conf import settings

from .models import About, AboutImages


class AboutImagesSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = AboutImages
        fields = ['thumbnail']

    def get_thumbnail(self, obj):
        if obj.thumbnail:
            image_url = obj.thumbnail.url
            path = '{domain}{path}'.format(domain=settings.BACK_URL, path=image_url)
            try:
                w, h = get_image_dimensions(obj.thumbnail.file)
                img = open(obj.capture.path, 'rb').read()
                data_base64 = base64.b64encode(img)
                byte_to_string = data_base64.decode('utf-8')
                data = {
                    'src': path,
                    'weight': w,
                    'height': h,
                    'base64': "data:image/jpg;base64," + byte_to_string,
                }
                return data
            except Exception:
                return None
        else:
            return None


class AboutSerializer(serializers.ModelSerializer):
    images = AboutImagesSerializer(many=True)

    class Meta:
        model = About
        fields = ['description', 'images' ]
