import base64
from django.core.files.images import get_image_dimensions
from rest_framework import serializers

from .models import News, NewsImages


class NewsImagesSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = NewsImages
        fields = ['thumbnail']

    def get_thumbnail(self, obj):
        request = self.context.get('request')
        if obj.thumbnail:
            image_url = obj.thumbnail.url
            path = request.build_absolute_uri(image_url)
            try:
                w, h = get_image_dimensions(obj.thumbnail.file)
                img = open(obj.capture.path, 'rb').read()
                data_base64 = base64.b64encode(img)
                byte_to_str = data_base64.decode("utf-8")
                data = {
                    'src': path,
                    'width': w,
                    'height': h,
                    'base64': "data:image/jpg;base64," + byte_to_str,
                }
                return data
            except Exception:
                return None
        else:
            return None


class NewsListSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['slug', 'title', 'thumbnail',
                  'views', 'pub_date']

    def get_thumbnail(self, obj):
        request = self.context.get('request')
        if obj.thumbnail:
            image_url = obj.thumbnail.url
            path = request.build_absolute_uri(image_url)
            try:
                w, h = get_image_dimensions(obj.thumbnail.file)
                img = open(obj.capture.path, 'rb').read()
                data_base64 = base64.b64encode(img)
                byte_to_str = data_base64.decode("utf-8")
                data = {
                    'src': path,
                    'width': w,
                    'height': h,
                    'base64': "data:image/jpg;base64," + byte_to_str,
                }
                return data
            except Exception:
                return None
        else:
            return None


class NewsDetailSerializer(serializers.ModelSerializer):
    images = NewsImagesSerializer(many=True)

    class Meta:
        model = News
        fields = ['images', 'title', 'content', 'views',
                  'pub_date', 'on_slider']
