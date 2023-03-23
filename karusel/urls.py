from django.urls import path

from .views import KaruselApiView


urlpatterns = [
    path('', KaruselApiView.as_view()),
]
