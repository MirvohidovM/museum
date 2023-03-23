from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Karusel
from .serializers import KaruselSerializer


class KaruselApiView(APIView):
    queryset = Karusel.objects.all()
    serializer_class = KaruselSerializer

    def get(self, request, format=None):
        queryset = Karusel.objects.get(pk=1)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)
