from django.urls import path
from studentDetailed import views

urlpatterns = [
    path('listCreate/', views.studentDetailedListCreate.as_view()),
    path('crud/<pk>/', views.studentDetailedCRUD.as_view()),
]