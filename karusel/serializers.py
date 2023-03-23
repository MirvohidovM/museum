from rest_framework import serializers
from django.core.files.images import get_image_dimensions
from django.conf import settings

from .models import Karusel, KaruselImages


class KaruselImagesSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('get_image')

    class Meta:
        model = KaruselImages
        fields = ['image', 'id']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            path = '{domain}{path}'.format(domain=settings.BACK_URL, path=image_url)
            try:
                w, h = get_image_dimensions(obj.image.file)
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


class KaruselSerializer(serializers.ModelSerializer):
    images = KaruselImagesSerializer(many=True)

    class Meta:
        model = Karusel
        fields = [ 'title', 'images']
