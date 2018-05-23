# from django.shortcuts import render


# Importing all the requirements
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from registration.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User,Group
from profBasic.models import profBasic
from profDetailed.models import profDetailed
from studentBasic.models import studentBasic
from studentDetailed.models import studentDetailed


class StudentCreate(APIView):
    """
    Creates the student User.
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

                sb = studentBasic.objects.create(username=json['username'])
                sd = studentDetailed.objects.create(username=json['username'])

                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfCreate(APIView):
    """
    Creates the professor User.
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

                pb = profBasic.objects.create(username=json['username'])
                pd = profDetailed.objects.create(username=json['username'])

                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
