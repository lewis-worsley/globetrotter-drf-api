from django.urls import path
from journeys import views

urlpatterns = [
    path('journeys/', views.JourneyList.as_view()),
    path('journeys/<int:pk>/', views.JourneyDetail.as_view()),
]
