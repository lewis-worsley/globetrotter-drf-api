from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import News
from .serializers import NewsSerializer

class NewsList(generics.ListCreateAPIView):
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = News.objects.all()

    filter_backends = [
        DjangoFilterBackend,
    ]


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = News.objects.all()