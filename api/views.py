from rest_framework import generics, permissions
from . import serializers
from django.contrib.auth.models import User
from .models import Post, Comments, Categories
from .permissions import CheckOwner


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckOwner]


class CommentsList(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = serializers.CommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = serializers.CommentsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckOwner]


class CategoriesList(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = serializers.CategoriesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoriesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categories.objects.all()
    serializer_class = serializers.CategoriesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, CheckOwner]