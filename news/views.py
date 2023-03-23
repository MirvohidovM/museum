from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import django_filters
from django_filters import rest_framework as filters
from django.db.models import Q

from config.paginations import CustomPagination
from .models import News
from .serializers import NewsDetailSerializer, NewsListSerializer


class NewsRetrieveAPIView(generics.RetrieveAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = News.objects.filter(is_active=True)
    serializer_class = NewsDetailSerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.views = obj.views + 1
        obj.save(update_fields=['views', ])
        serializer = self.get_serializer(obj)
        return Response(serializer.data, status=200)


class NewsFilter(django_filters.FilterSet):
    on_slider = filters.CharFilter(
        field_name='on_slider', method='filter_on_slider')

    content = filters.CharFilter(
        field_name='content', method='filter_content')

    year = filters.CharFilter(
        field_name='year', method='filter_year')

    month = filters.CharFilter(
        field_name='month', method='filter_month')

    date = filters.CharFilter(
        field_name='date', method='filter_date')

    class Meta:
        model = News
        fields = ['content', 'year', 'month', 'date', 'on_slider']

    def filter_content(self, queryset, name, value):
        q = queryset.filter(Q(title__icontains=value.lower())
                            | Q(content__icontains=value.lower()))
        return q

    def filter_year(self, queryset, name, value):
        q = queryset.filter(
            pub_date__year=value)
        return q

    def filter_month(self, queryset, name, value):
        q = queryset.filter(
            pub_date__month=value)
        return q

    def filter_date(self, queryset, name, value):
        q = queryset.filter(
            pub_date=value)
        return q

    def filter_on_slider(self, queryset, name, value):
        q = queryset.filter(
            on_slider=True)
        return q


class NewsListAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    pagination_class = CustomPagination
    queryset = News.objects.filter(is_active=True)
    serializer_class = NewsListSerializer
    filterset_class = NewsFilter


class NewsHomeListAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = News.objects.filter(is_active=True).order_by('-pub_date')[0:4]
    serializer_class = NewsListSerializer


