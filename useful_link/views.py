from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from useful_link import serializers
from useful_link.models import UsefulLink


class UsefulLinkListView(ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = serializers.UsefulLinkListSerializer

    def get_queryset(self):
        queryset = UsefulLink.objects.all().order_by('-created_at')[0:4]
        return queryset
