from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from globetrotter_drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view (post method), as profile creation handled by Django signals
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        journeys_count=Count('owner__journey', distinct=True),
        blogs_count=Count('owner__blog', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    ordering_fields = [
        'journeys_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]
    filterset_fields = [
        # Filter profiles that are following a profile given its ID
        'owner__following__followed__profile',  # 1
        # Filter profiles that are followed by a profile, given its ID
        'owner__followed__owner__profile',  # 2
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        journeys_count=Count('owner__journey', distinct=True),
        blogs_count=Count('owner__blog', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
