from django.urls import path
from likes_stops import views

urlpatterns = [
    path('stops/likes/', views.LikeStopList.as_view()),
    path('stops/likes/<int:pk>/', views.LikeStopDetail.as_view()),
]