from django.urls import path
from profBasic import views

urlpatterns = [
    path('listCreate/', views.profBasicListCreate.as_view()),
    path('crud/<pk>/', views.profBasicCRUD.as_view()),
]