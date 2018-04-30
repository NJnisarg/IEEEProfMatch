from django.shortcuts import render
from studentBasic.models import studentBasic
from studentBasic.serializers import studentBasicSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# class studentBasicListCreate(APIView):
#     """
#         List all basicInfos, or create a new basicInfo.
#     """
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)

#     def get(self, request, format=None):
#         basics = studentBasic.objects.all()
#         serializer = studentBasicSerializer(basics, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = studentBasicSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class studentBasicCRUD(APIView):
    """
    Retrieve or update a basicInfo instance.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return studentBasic.objects.get(pk=pk)
        except studentBasic.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        basicInfo = self.get_object(pk)
        serializer = studentBasicSerializer(basicInfo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        basicInfo = self.get_object(pk)
        serializer = studentBasicSerializer(basicInfo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk, format=None):
    #     basicInfo = self.get_object(pk)
    #     basicInfo.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
