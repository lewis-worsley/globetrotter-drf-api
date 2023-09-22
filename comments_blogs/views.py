from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from globetrotter_drf_api.permissions import IsOwnerOrReadOnly
from .models import CommentBlog
from .serializers import CommentBlogSerializer, CommentBlogDetailSerializer


class CommentBlogList(generics.ListCreateAPIView):
    serializer_class = CommentBlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = CommentBlog.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    filter_backends = [
        DjangoFilterBackend
    ]
    filterset_fields = [
        # Be able to retrieve all the comments associated with a given blog
        'blog'
    ]


class CommentBlogDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentBlogDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = CommentBlog.objects.all()
