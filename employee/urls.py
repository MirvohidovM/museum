from django.urls import path
from .views import EmployeeListAPIView #, EmployeeLidershipListAPIView

urlpatterns = [
    path('hodimlar/', EmployeeListAPIView.as_view(), name='employee-list'),
    path('xodimlar/', EmployeeListAPIView.as_view(), name='employee-list'),

    # path('rahbariyat/', EmployeeLidershipListAPIView.as_view(), name='employee-detail'),
]
