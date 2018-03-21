from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/student/', views.StudentCreate.as_view(), name='student-register'),
    url(r'^register/prof/', views.ProfCreate.as_view(), name='prof-register'),
]