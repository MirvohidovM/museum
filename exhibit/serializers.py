import base64
from rest_framework import serializers
from django.core.files.images import get_image_dimensions

from exhibit.models import Exhibit, Category, ExhibitImages


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('slug', 'name', 'logo',)


class ExhibitImagesListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = ExhibitImages
        fields = ('image',)

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            path = request.build_absolute_uri(image_url)
            try:
                w, h = get_image_dimensions(obj.image.file)
                img = open(obj.capture.path, 'rb').read()
                data_base64 = base64.b64encode(img)
                byte_to_string = data_base64.decode('utf-8')
                data = {
                    "src": path,
                    'weight': w,
                    "height": h,
                    "base64": "data:image/jpg;base64," + byte_to_string,
                }
                return data
            except Exception:
                return None
        else:
            return None


class ExhibitListSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Exhibit
        fields = ('slug', 'name', 'summary', 'thumbnail')

    def get_thumbnail(self, obj):
        request = self.context.get('request')
        if obj.thumbnail:
            image_url = obj.thumbnail.url
            path = request.build_absolute_uri(image_url)
            try:
                w, h = get_image_dimensions(obj.thumbnail.file)
                img = open(obj.capture.path, 'rb').read()
                data_base64 = base64.b64encode(img)
                byte_to_string = data_base64.decode('utf-8')
                data = {
                    "src": path,
                    'weight': w,
                    "height": h,
                    "base64": "data:image/jpg;base64," + byte_to_string,
                }
                return data
            except Exception:
                return None
        else:
            return None


class ExhibitDetailSerializer(serializers.ModelSerializer):
    images = ExhibitImagesListSerializer(many=True, read_only=True)
    cover = serializers.SerializerMethodField()
    category = serializers.SlugRelatedField(slug_field='slug', read_only=True)

    class Meta:
        model = Exhibit
        fields = ('name', 'summary', 'used_years', 'invented_year',
                  'body', 'audio', 'gif', 'cover',  'images', 'category')

    def get_cover(self, obj):
        request = self.context.get('request')
        if obj.cover:
            image_url = obj.cover.url
            path = request.build_absolute_uri(image_url)
            try:
                w, h = get_image_dimensions(obj.cover.file)
                img = open(obj.capture.path, 'rb').read()
                data_base64 = base64.b64encode(img)
                byte_to_string = data_base64.decode('utf-8')
                data = {
                    "src": path,
                    'weight': w,
                    "height": h,
                    "base64": "data:image/jpg;base64," + byte_to_string,
                }
                return data
            except Exception:
                return None
        else:
            return None


class EvolutionSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Exhibit
        fields = ('slug', 'thumbnail', 'invented_year')

    def get_thumbnail(self, obj):
        request = self.context.get('request')
        if obj.thumbnail:
            image_url = obj.thumbnail.url
            path = request.build_absolute_uri(image_url)
            try:
                w, h = get_image_dimensions(obj.thumbnail.file)
                img = open(obj.capture.path, 'rb').read()
                data_base64 = base64.b64encode(img)
                byte_to_string = data_base64.decode('utf-8')
                data = {
                    "src": path,
                    'weight': w,
                    "height": h,
                    "base64": "data:image/jpg;base64," + byte_to_string,
                }
                return data
            except Exception:
                return None
        else:
            return None
