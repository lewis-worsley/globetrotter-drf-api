from django.db.models import Count
from rest_framework import generics, permissions, filters
from .models import Stop
from .serializers import StopSerializer
from globetrotter_drf_api.permissions import IsOwnerOrReadOnly


class StopList(generics.ListCreateAPIView):
    """
    List stops or create a stop if logged in.
    The perform_create method associates the stop with the logged in user.
    """
    serializer_class = StopSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Stop.objects.annotate(
        likes_count = Count('likes', distinct=True),
        comments_count = Count('commentstop', distinct=True),
    ).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StopDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a stop and edit or delete it if you own it.
    """
    serializer_class = StopSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Stop.objects.annotate(
        likes_count = Count('likes', distinct=True),
        comments_count = Count('commentstop', distinct=True),
    ).order_by('-created_at')