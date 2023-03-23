import base64
from rest_framework import serializers
from django.core.files.images import get_image_dimensions
from rest_framework.serializers import ModelSerializer

from gallery.models import PhotoGallery, PhotoGalleryImages


class PhotoGalleryImagesSerializer(ModelSerializer):
    # thumbnail = serializers.SerializerMethodField("get_thumbnail")

    class Meta:
        model = PhotoGalleryImages
        fields = ['image']

    # def get_thumbnail(self, obj):
    #     request = self.context.get('request')
    #     if obj.thumbnail:
    #         image_url = obj.thumbnail.url
    #         path = request.build_absolute_uri(image_url)
    #         try:
    #             w, h = get_image_dimensions(obj.thumbnail.file)
    #             img = open(obj.capture.path, 'rb').read()
    #             data_base64 = base64.b64encode(img)
    #             byte_to_string = data_base64.decode('utf-8')
    #             data = {
    #                 "src": path,
    #                 'weight': w,
    #                 "height": h,
    #                 "base64": "data:image/jpg;base64," + byte_to_string,
    #             }
    #             return data
    #         except Exception:
    #             return None
    #     else:
    #         return None


class PhotoGalleryListSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = PhotoGallery
        fields = ['slug', 'title', 'thumbnail']

    def get_thumbnail(self, obj):
        request = self.context.get('request')
        if obj.thumbnail:
            image_url = obj.thumbnail.url
            path = request.build_absolute_uri(image_url)
            try:
                w,h = get_image_dimensions(obj.thumbnail.file)
                img = open(obj.capture.path, 'rb').read()
                data_base64 = base64.b64encode(img)
                byte_to_string = data_base64.decode('utf-8')
                data = {
                    'src': path,
                    'weight': w,
                    'height': h,
                    'base64': "data:image/jpg;base64," + byte_to_string
                }
                return data
            except Exception:
                return None
        else:
            return None


class PhotoGalleryDetailSerializer(serializers.ModelSerializer):
    images = PhotoGalleryImagesSerializer(many=True)
    class Meta:
        model = PhotoGallery
        fields = ['slug', 'photo', 'images']
