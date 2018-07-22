from studentList.serializers import studentListSerializer
from studentList.workers import getList
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class studentListAPI(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk,format=None):
        stuList = getList(pk)
        serializer = studentListSerializer(stuList, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
