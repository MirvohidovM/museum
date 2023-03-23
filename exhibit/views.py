from rest_framework import generics, filters
from django.db.models import Q

from config.paginations import CustomPagination
from exhibit.models import Category, Exhibit
from exhibit.serializers import (CategoryListSerializer, ExhibitListSerializer,
                                 ExhibitDetailSerializer, EvolutionSerializer,)


class CategoryHomeListAPIView(generics.ListAPIView):
    queryset = Category.objects.filter(~Q(logo='')).filter(to_main_page=True)[0:4]
    serializer_class = CategoryListSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class ExhibitSearchListAPIView(generics.ListAPIView):
    queryset = Exhibit.objects.all()
    pagination_class = CustomPagination
    serializer_class = ExhibitListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class ExhibitDetailAPIView(generics.RetrieveAPIView):
    queryset = Exhibit.objects.all()
    serializer_class = ExhibitDetailSerializer
    lookup_field = 'slug'


class ExhibitHomeListAPIView(generics.ListAPIView):
    queryset = Exhibit.objects.all().filter(to_main_page=True)
    serializer_class = ExhibitListSerializer


class EvolutionAPIView(generics.ListAPIView):
    queryset = Exhibit.objects.filter(to_about_page=True)
    serializer_class = EvolutionSerializer


class ExhibitsByCategoryView(generics.ListAPIView):
    serializer_class = ExhibitListSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        slug = self.kwargs['category_slug']
        queryset = Exhibit.objects.filter(category__slug=slug)
        return queryset


class ExhibitsThreeByCategoryView(generics.ListAPIView):
    serializer_class = ExhibitListSerializer

    def get_queryset(self):
        slug = self.kwargs['category_slug']
        queryset = Exhibit.objects.filter(category__slug=slug).order_by('-created_at')[0:3]
        return queryset