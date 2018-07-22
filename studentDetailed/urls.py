from django.urls import path
from studentDetailed import views

urlpatterns = [
    path('crud/<pk>/', views.studentDetailedCRUD.as_view()),
]