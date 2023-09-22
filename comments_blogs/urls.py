from django.urls import path
from comments_blogs import views

urlpatterns = [
    path('blogs/comments/', views.CommentBlogList.as_view()),
    path('blogs/comments/<int:pk>/', views.CommentBlogDetail.as_view()),
]
