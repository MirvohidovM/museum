from django.conf import settings
from django.core.files.images import get_image_dimensions
from rest_framework import serializers

from useful_link.models import UsefulLink


class UsefulLinkListSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = UsefulLink
        fields = ['slug', 'title', 'link', 'image']

    def get_image(self, obj):
        request = self.context.get('request')

        if obj.image:
            image_url = obj.image.url
            # path = f"https//:{settings.DOMAIN}{image_url}"
            path = request.build_absolute_uri(image_url)
            try:
                w, h = get_image_dimensions(obj.image.file)
                data = {
                    'src': path,
                    'width': w,
                    'height': h,
                }
                return data
            except Exception:
                return None
        else:
            return None
