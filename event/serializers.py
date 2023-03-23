import base64
from django.core.files.images import get_image_dimensions
from rest_framework import serializers

from .models import Event, EventType, EventImages


class EventImagesSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField('get_thumbnail')

    class Meta:
        model = EventImages
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


class EventDetailSerializer(serializers.ModelSerializer):
    images = EventImagesSerializer(many=True)

    class Meta:
        model = Event
        fields = ['slug', 'title', 'content', 'images', 'start_time', 'num_visitors',
                 'responsible_org', 'pub_date', 'views', 'on_slider' ]


class EventListSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField('get_image')
    type = serializers.SlugRelatedField(read_only=True, slug_field='title')

    class Meta:
        model = Event
        fields = ["slug", 'title', 'start_time', 'thumbnail', 'num_visitors',
                  'responsible_org', "pub_date", 'type']

    def get_image(self, obj):
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
