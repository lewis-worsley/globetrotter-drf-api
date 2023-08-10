from django.urls import path
from comments_stops import views

urlpatterns = [
    path('journeys/stops/comments/', views.CommentStopList.as_view()),
    path('journeys/stops/comments/<int:pk>/', views.CommentStopDetail.as_view()),
]