from django.urls import path
from studentBasic import views

urlpatterns = [
    path('crud/<pk>/', views.studentBasicCRUD.as_view()),
]
