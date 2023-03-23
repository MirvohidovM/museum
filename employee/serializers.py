from rest_framework import serializers
from django.conf import settings
from django.core.files.images import get_image_dimensions

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['slug', 'name', 'position', 'email', 'phone', 'thumbnail', 'index']

    def get_thumbnail(self, obj):
        if obj.thumbnail_240:
            photo_url = obj.thumbnail_240.url
            path = '{domain}{path}'.format(
                domain=settings.BACK_URL, path=photo_url)
            try:
                w, h = get_image_dimensions(obj.thumbnail_240.file)
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
