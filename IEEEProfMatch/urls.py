"""IEEEProfMatch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AuthReg/', include('registration.urls'), name='register'),
    path('Auth/', include('login.urls'), name='login'),
    path('studentBasic/', include('studentBasic.urls'), name='studentBasic'),
    path('profBasic/', include('profBasic.urls'), name='profBasic'),
    path('studentDetailed/', include('studentDetailed.urls'), name='studentDetailed'),
    path('profDetailed/', include('profDetailed.urls'), name='profDetailed'),
    path('studentList/', include('studentList.urls'), name='studentList'),
]
