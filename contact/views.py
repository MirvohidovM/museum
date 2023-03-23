from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ContactSerializer, LandmarkPhotosSerializer
from .models import Contact, LandmarkPhotos


class ContactAPIView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny, ]
    serializer_class = ContactSerializer

    def get(self, request, format=None):
        queryset = Contact.objects.get(pk=1)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)
