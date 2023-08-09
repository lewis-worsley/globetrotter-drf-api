from django.urls import path
from comments import views

urlpatterns = [
    path('journeys/comments/', views.CommentList.as_view()),
    path('journeys/comments/<int:pk>/', views.CommentDetail.as_view()),
]