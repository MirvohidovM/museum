from django.urls import path

from .views import OrderCreateApiView, ExcursionTypeAPIView


urlpatterns = [
    path('excursion_type/', ExcursionTypeAPIView.as_view()),
    path('create/', OrderCreateApiView.as_view()),
]
