from django.urls import path

from gallery import views

urlpatterns = [
    path('photo/', views.PhotoGalleryListAPIView.as_view()),
    path('photo/<slug>/', views.PhotoGalleryDetailAPIView.as_view()),
]
