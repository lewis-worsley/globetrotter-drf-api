from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Blog
from .serializers import BlogSerializer
from globetrotter_drf_api.permissions import IsOwnerOrReadOnly


class BlogList(generics.ListCreateAPIView):
    """
    List journeys (posts) or create a journey if logged in.
    The perform_create method associates the journey with the logged in user.
    """
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Blog.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a journey (post) and edit or delete it if you own it.
    """
    serializer_class = BlogSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Blog.objects.all()
