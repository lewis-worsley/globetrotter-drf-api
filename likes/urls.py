from django.urls import path
from likes import views

urlpatterns = [
    path('journeys/likes/', views.LikeList.as_view()),
    path('journeys/likes/<int:pk>/', views.LikeDetail.as_view()),
]