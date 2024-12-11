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


class UserRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
