from rest_framework import serializers

from posts.models import Post, User


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('text', 'pub_date', 'author')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        models = User
        fields = ('id', 'username',)
