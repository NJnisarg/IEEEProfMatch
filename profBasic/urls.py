from django.urls import path
from profBasic import views

urlpatterns = [
    path('crud/<pk>/', views.profBasicCRUD.as_view()),
]