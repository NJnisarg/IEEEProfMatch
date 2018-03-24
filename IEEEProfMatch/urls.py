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
    url(r'^AuthReg/', include('registration.urls')),
    url(r'^Auth/',include('login.urls')),
    url(r'^studentBasic/',include('studentBasic.urls')),
    url(r'^profBasic/',include('profBasic.urls')),
    url(r'^studentDetailed/',include('studentDetailed.urls')),
    url(r'^profDetailed/',include('profDetailed.urls')),
    url(r'^studentList/',include('studentList.urls')),
]
