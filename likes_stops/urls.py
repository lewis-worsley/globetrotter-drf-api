from django.urls import path
from likes_stops import views

urlpatterns = [
    path('journeys/stops/likes/', views.LikeStopList.as_view()),
    path('journeys/stops/likes/<int:pk>/', views.LikeStopDetail.as_view()),
]