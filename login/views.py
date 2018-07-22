
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from login.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class login(APIView):
    """
    logs in the user.
    """
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(username=serializer.data['username'], password=serializer.data['password'])
            if user is not None:
                token = Token.objects.get(user=user)
                group = user.groups.all()[0].name
                json = serializer.data
                json['token'] = token.key
                json['type'] = group
                return Response(json, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
