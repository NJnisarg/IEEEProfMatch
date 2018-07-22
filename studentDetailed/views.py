from studentDetailed.models import studentDetailed
from studentDetailed.serializers import studentDetailedSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class studentDetailedCRUD(APIView):
    """
    Retrieve or update a detailInfo instance.
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return studentDetailed.objects.get(pk=pk)
        except studentDetailed.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        detailInfo = self.get_object(pk)
        serializer = studentDetailedSerializer(detailInfo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        detailInfo = self.get_object(pk)
        serializer = studentDetailedSerializer(detailInfo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

