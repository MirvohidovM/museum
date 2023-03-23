from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from config.paginations import CustomPagination

from .models import Employee
from .serializers import EmployeeSerializer  #, EmployeeLidershipSerializer


class EmployeeListAPIView(ListAPIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    serializer_class = EmployeeSerializer
    
    def get_queryset(self):
        queryset = Employee.objects.exclude(name__isnull=True)#.filter(is_lidership=False)
        return queryset


# class EmployeeLidershipListAPIView(ListAPIView):
#     authentication_classes = []
#     permission_classes = [AllowAny]
#     pagination_class = CustomPagination
#     filter_backends = [DjangoFilterBackend]
#     # filterset_fields = []
#     serializer_class = EmployeeLidershipSerializer
#
#     def get_queryset(self):
#         queryset = Employee.objects.exclude(name__isnull=True).filter(is_lidership=True)
#         return queryset
