from django.shortcuts import render
from profDetailed.models import profDetailed
from profDetailed.serializers import profDetailedSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.


class profDetailedListCreate(APIView):
    """
    List all detailInfos, or create a new detailInfo.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        details = profDetailed.objects.all()
        serializer = profDetailedSerializer(details, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = profDetailedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class profDetailedCRUD(APIView):
    """
    Retrieve, update or delete a detailInfo instance.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    def get_object(self, pk):
        try:
            return profDetailed.objects.get(pk=pk)
        except profDetailed.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        detailInfo = self.get_object(pk)
        serializer = profDetailedSerializer(detailInfo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        detailInfo = self.get_object(pk)
        serializer = profDetailedSerializer(detailInfo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        detailInfo = self.get_object(pk)
        detailInfo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
