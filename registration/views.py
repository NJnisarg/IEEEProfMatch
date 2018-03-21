# from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from registration.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User,Group


class StudentCreate(APIView):
    """
    Creates the user.
    """
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                group = Group.objects.get(name='student')
                user.groups.add(group)
                json = serializer.data
                json['token'] = token.key
                json['type'] = 'student'
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfCreate(APIView):
    """
    Creates the user.
    """

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                group = Group.objects.get(name='prof')
                user.groups.add(group)
                json = serializer.data
                json['token'] = token.key
                json['type'] = 'prof'
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
