from django.urls import path
from comments_stops import views

urlpatterns = [
    path('stops/comments/', views.CommentStopList.as_view()),
    path('stops/comments/<int:pk>/', views.CommentStopDetail.as_view()),
]