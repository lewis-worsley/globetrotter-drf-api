from rest_framework import generics, permissions
from globetrotter_drf_api.permissions import IsOwnerOrReadOnly
from .models import LikeStop
from .serializers import LikeStopSerializer


class LikeStopList(generics.ListCreateAPIView):
    serializer_class = LikeStopSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = LikeStop.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeStopDetail(generics.RetrieveDestroyAPIView):
    serializer_class = LikeStopSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = LikeStop.objects.all()