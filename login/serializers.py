from rest_framework import serializers
from django.contrib.auth.models import User,Group


class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(
        required=True,
    )
    username = serializers.CharField(
        max_length=32,
        required=True
    )
    password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        fields = ('username','email', 'password')

