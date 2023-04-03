"""Kulimo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path
from django.views.generic import RedirectView
#from accueil.views import register_request, login_request
from accueil.views import *

urlpatterns = [
    #path('', include('accueil.urls')), 
    path('', RedirectView.as_view(url='/accueil')), 
    path('accueil/', include('accueil.urls')),
    path('admin/', admin.site.urls),
    path('register/', register_request, name='register'),
    path('login/', login_request, name='login'),
    path('a_propos_de_nous/', include('accueil.urls')),
    path('nous_joindre/', include('accueil.urls'))
]
