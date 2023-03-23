from django.urls import path
from .views import AboutAPIView


urlpatterns = [
    path('', AboutAPIView.as_view(), name='about'),
]
