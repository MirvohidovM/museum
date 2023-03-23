from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsListAPIView.as_view()),
    path('<slug>', views.NewsRetrieveAPIView.as_view()),
    path('homepage/', views.NewsHomeListAPIView.as_view()),
]
