from django.urls import path

from exhibit.views import (ExhibitSearchListAPIView,
                           ExhibitDetailAPIView,
                           EvolutionAPIView,
                           ExhibitHomeListAPIView,
                           ExhibitsByCategoryView,
                           CategoryHomeListAPIView,
                           CategoryListAPIView,
                           ExhibitsThreeByCategoryView)


urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('bycategory/<category_slug>', ExhibitsByCategoryView.as_view()),
    path('bycategory/<category_slug>/three', ExhibitsThreeByCategoryView.as_view()),

    path('', ExhibitSearchListAPIView.as_view()),
    path('<slug>', ExhibitDetailAPIView.as_view()),
    path('about/', EvolutionAPIView.as_view()),

    path('homepage/', ExhibitHomeListAPIView.as_view()),
    path('categories/homepage/', CategoryHomeListAPIView.as_view()),
]
