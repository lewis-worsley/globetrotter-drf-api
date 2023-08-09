from rest_framework import generics, permissions, filters
from .models import Stops
from .serializers import StopsSerializer
from globetrotter_drf_api.permissions import IsOwnerOrReadOnly


class StopsList(generics.ListCreateAPIView):
    """
    List stops or create a stop if logged in.
    The perform_create method associates the stop with the logged in user.
    """
    serializer_class = StopsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Stops.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class StopsDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a stop and edit or delete it if you own it.
    """
    serializer_class = StopsSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Stops.objects.all()