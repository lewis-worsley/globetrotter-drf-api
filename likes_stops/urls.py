from django.urls import path
from likes_stops import views

urlpatterns = [
    path('likesstops/', views.LikeStopList.as_view()),
    path('likesstops/<int:pk>/', views.LikeStopDetail.as_view()),
]