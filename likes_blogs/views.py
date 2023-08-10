from rest_framework import generics, permissions
from globetrotter_drf_api.permissions import IsOwnerOrReadOnly
from .models import LikeBlog
from .serializers import LikeBlogSerializer


class LikeBlogList(generics.ListCreateAPIView):
    serializer_class = LikeBlogSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = LikeBlog.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeBlogDetail(generics.RetrieveDestroyAPIView):
    serializer_class = LikeBlogSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = LikeBlog.objects.all()