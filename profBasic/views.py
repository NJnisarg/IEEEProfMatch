from django.shortcuts import render
from profBasic.models import profBasic
from profBasic.serializers import profBasicSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.


class profBasicListCreate(APIView):
    """
    List all basicInfos, or create a new basicInfo.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        basics = profBasic.objects.all()
        serializer = profBasicSerializer(basics, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = profBasicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class profBasicCRUD(APIView):
    """
    Retrieve, update or delete a basicInfo instance.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return profBasic.objects.get(pk=pk)
        except profBasic.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        basicInfo = self.get_object(pk)
        serializer = profBasicSerializer(basicInfo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        basicInfo = self.get_object(pk)
        serializer = profBasicSerializer(basicInfo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        basicInfo = self.get_object(pk)
        basicInfo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
