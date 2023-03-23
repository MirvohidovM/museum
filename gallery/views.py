from rest_framework.permissions import AllowAny
from rest_framework import generics

from config.paginations import CustomPagination
from gallery.models import PhotoGallery
from gallery.serializers import PhotoGalleryListSerializer, PhotoGalleryDetailSerializer


class PhotoGalleryDetailAPIView(generics.RetrieveAPIView):
    queryset = PhotoGallery.objects.all()
    serializer_class = PhotoGalleryDetailSerializer
    lookup_field = 'slug'


class PhotoGalleryListAPIView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    queryset = PhotoGallery.objects.all()
    serializer_class = PhotoGalleryListSerializer
    pagination_class = CustomPagination
