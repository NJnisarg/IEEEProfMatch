# Importing all the requirements
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User,Group

from registration.serializers import UserSerializer

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


class ProfRemove(APIView):
    """
    Deletes the professor user
    """
    def delete(self, request, pk, format='json'):
        user = User.objects.get(username=pk)
        pb = profBasic.objects.get(username=pk)
        pd = profDetailed.objects.get(username=pk)

        if (user is not None) and (pb is not None) and (pd is not None):
            user.delete()
            pb.delete()
            pd.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


class StudentRemove(APIView):
    """
    Deletes the student user
    """
    def delete(self, request, pk, format='json'):
        user = User.objects.get(username=pk)
        sb = studentBasic.objects.get(username=pk)
        sd = studentDetailed.objects.get(username=pk)

        if (user is not None) and (sb is not None) and (sd is not None):
            user.delete()
            sb.delete()
            sd.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
