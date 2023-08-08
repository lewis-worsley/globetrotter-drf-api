from django.db.models import Count
from rest_framework import generics, permissions, filters
from .models import Journey
from .serializers import JourneySerializer
from globetrotter_drf_api.permissions import IsOwnerOrReadOnly


class JourneyList(generics.ListCreateAPIView):
    """
    List journeys (posts) or create a post if logged in.
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = JourneySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Journey.objects.annotate(
        likes_count = Count('likes', distinct=True),
        comments_count = Count('comment', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class JourneyDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a journey (post) and edit or delete it if you own it.
    """
    serializer_class = JourneySerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Journey.objects.annotate(
        likes_count = Count('likes', distinct=True),
        comments_count = Count('comment', distinct=True),
    ).order_by('-created_at')
