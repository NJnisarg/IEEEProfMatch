from django.urls import path
from profBasic import views

urlpatterns = [
    path('crud/<pk>/', views.profBasicCRUD.as_view()),
    path('profImage/list/', views.ImageList.as_view()),
    path('profImage/crud/<pk>/', views.ImageDetail.as_view()),
]