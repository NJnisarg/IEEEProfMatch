from profDetailed import views
from django.urls import path

urlpatterns = [
    path('crud/<pk>/', views.profDetailedCRUD.as_view()),
    path('studentList/<pk>/', views.profDetailedStudentList.as_view())
]

