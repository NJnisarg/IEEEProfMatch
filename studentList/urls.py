from django.urls import path
from studentList.views import studentListAPI

urlpatterns = [
    path('get/<pk>/', studentListAPI.as_view()),
]