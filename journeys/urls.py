from django.urls import path
from journeys import views

urlpatterns = [
    path('journeys/', views.JourneyList.as_view()),
]