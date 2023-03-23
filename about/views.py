from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .models import About
from .serializers import AboutSerializer, AboutImagesSerializer
from rest_framework.response import Response


class AboutAPIView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny, ]
    serializer_class = AboutSerializer
    # queryset = About.objects.all()

    def get(self, request, format=None):
        queryset = About.objects.get(pk=1)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)
