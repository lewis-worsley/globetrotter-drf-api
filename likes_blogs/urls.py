from django.urls import path
from likes_blogs import views

urlpatterns = [
    path('blogs/likes/', views.LikeBlogList.as_view()),
    path('blogs/likes/<int:pk>/', views.LikeBlogDetail.as_view()),
]
