from rest_framework import viewsets
from rest_framework.views import APIView

from posts.models import Post, User

from .serializers import (
    PostSerializer, UserSerializer, UserRegistrationSerializer
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
