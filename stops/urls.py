from django.urls import path
from stops import views

urlpatterns = [
    path('journeys/stops/', views.StopList.as_view()),
    path('journeys/stops/<int:pk>/', views.StopDetail.as_view()),
]
