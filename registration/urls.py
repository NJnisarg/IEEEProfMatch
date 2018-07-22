from django.urls import path
from . import views

urlpatterns = [
    path('register/student/', views.StudentCreate.as_view(), name='student-register'),
    path('register/prof/', views.ProfCreate.as_view(), name='prof-register'),
    path('remove/student/<pk>/', views.StudentRemove.as_view(), name='student-remove'),
    path('remove/prof/<pk>/', views.ProfRemove.as_view(), name='prof-remove'),
]