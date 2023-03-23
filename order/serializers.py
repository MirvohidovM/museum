from rest_framework import serializers

from .models import Order, ExcursionType


class ExcursionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcursionType
        fields = ['id', 'name']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['firstname', 'lastname', 'email', 'phone', 'visit_time',
                  'num_visitors', 'organization', 'excursion_type', 'excursion_lan']
