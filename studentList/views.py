from profDetailed.models import profDetailed
from studentDetailed.models import studentDetailed
from studentList.serializers import studentListSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.

class studentListAPI(APIView):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk,format=None):
        prof = profDetailed.objects.get(pk=pk)
        stuList = studentDetailed.objects.filter(cgpa__gte=prof.minCgpa,yearOfStudy__gte=prof.minYearOfStudy,workEx__gte=prof.minWorkEx)
        serializer = studentListSerializer(stuList, many=True)
        return Response(serializer.data)