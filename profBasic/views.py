from profBasic.models import profBasic
from profBasic.serializers import profBasicSerializer, ImageSerializer
from django.http import Http404
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FileUploadParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class profBasicCRUD(APIView):
    """
    Retrieve or update a basicInfo instance.
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


class ImageList(generics.ListCreateAPIView):
    queryset = profBasic.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser, FileUploadParser, )


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = profBasic.objects.all()
    serializer_class = ImageSerializer
    parser_classes = (MultiPartParser, FormParser, FileUploadParser,)
