from rest_framework import generics, permissions
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
    queryset = Journey.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=.self.request.user)


class JourneyDetail(APIView):
    """
    Retrieve a journey (post) and edit or delete it if you own it.
    """
    serializer_class = JourneySerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Journey.objects.all()
