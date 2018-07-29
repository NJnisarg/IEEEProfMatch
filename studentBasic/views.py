from studentBasic.models import studentBasic
from studentBasic.serializers import studentBasicSerializer, ImageSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


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


class ImageList(generics.ListCreateAPIView):
    queryset = studentBasic.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser, FileUploadParser, )


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = studentBasic.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser, FileUploadParser,)


