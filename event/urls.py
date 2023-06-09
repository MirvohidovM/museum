from django.urls import path

from .views import EventListView, EventDetailView, EventHomeListView


urlpatterns = [
    path('', EventListView.as_view()),
    path('<slug>', EventDetailView.as_view()),
    path('homepage/', EventHomeListView.as_view()),
]
