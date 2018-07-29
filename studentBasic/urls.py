from django.urls import path
from studentBasic import views

urlpatterns = [
    path('crud/<pk>/', views.studentBasicCRUD.as_view()),
    path('studentImage/list/', views.ImageList.as_view()),
    path('studentImage/crud/<pk>/', views.ImageDetail.as_view()),
]
