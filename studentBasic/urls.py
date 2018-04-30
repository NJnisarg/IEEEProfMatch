from django.urls import path
from studentBasic import views

urlpatterns = [
    # path('listCreate/', views.studentBasicListCreate.as_view()),
    path('crud/<pk>/', views.studentBasicCRUD.as_view()),
]
