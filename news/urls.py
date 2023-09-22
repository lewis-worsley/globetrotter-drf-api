from django.urls import path
from news import views

urlpatterns = [
    path('news/', views.NewsList.as_view()),
    path('news/<int:pk>/', views.NewsDetail.as_view()),
]
