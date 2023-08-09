from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from globetrotter_drf_api.permissions import IsOwnerOrReadOnly
from .models import CommentStop
from .serializers import CommentStopSerializer, CommentStopDetailSerializer


class CommentStopList(generics.ListCreateAPIView):
    serializer_class = CommentStopSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = CommentStop.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        # Be able to retrieve all the comments associated with a given stop
        'stop', # 1
    ]


class CommentStopDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentStopDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = CommentStop.objects.all()