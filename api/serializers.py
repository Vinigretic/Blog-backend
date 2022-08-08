from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post, Comments, Categories


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'posts', 'comments', 'category']


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'owner', 'comments', 'category']


class CommentsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = Comments
        fields = ['id', 'body', 'owner', 'post']


class CategoriesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')


    class Meta:
        model = Categories
        fields = ['id', 'category_title', 'owner', 'post']
