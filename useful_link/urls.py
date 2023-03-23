from django.urls import path

from useful_link import views


urlpatterns = [
    path('homepage/', views.UsefulLinkListView.as_view()),
]
