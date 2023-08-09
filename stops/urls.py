from django.urls import path
from stops import views

urlpatterns = [
    path('journeys/stops/', views.StopsList.as_view()),
    path('journeys/stops/<int:pk>/', views.StopsDetail.as_view()),
]