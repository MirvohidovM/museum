from rest_framework import generics
from rest_framework.permissions import AllowAny
from dateutil import parser
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from config.paginations import CustomPagination

from .models import Event
from .serializers import EventDetailSerializer, EventListSerializer


class EventDetailView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = Event.objects.filter(is_active=True)
    serializer_class = EventDetailSerializer
    lookup_field = 'slug'

    def get_object(self):
        obj = super().get_object()
        obj.views = obj.views + 1
        obj.save(update_fields=['views', ])
        return obj


class EventFilter(django_filters.FilterSet):
    date = filters.CharFilter(field_name='date', method='filter_date')

    class Meta:
        model = Event
        fields = ['date']

    def filter_date(self, queryset, name, value):
        _model = self.Meta.model
        selected_date = parser.parse(value)
        filtered_result = _model.objects.filter(start_time__lte=selected_date,
        end_time__gte=selected_date)
        return filtered_result


class EventListView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = EventFilter
    queryset = Event.objects.filter(is_active=True).order_by('start_time')
    serializer_class = EventListSerializer


class EventHomeListView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = Event.objects.filter(is_active=True).order_by('start_time')[0:3]
    serializer_class = EventListSerializer
