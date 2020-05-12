from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
    age = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, request):
        """Creates and returns a new user"""
        user = models.UserProfile.objects.create_user(
            email=request['email'],
            name=request['name'],
            password=request['password']
        )

        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}

