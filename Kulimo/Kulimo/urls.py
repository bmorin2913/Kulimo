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
from accueil.views import register_request, login_request, logout_request, userposts_create_view, userposts_list_view, userposts_detail_view, profile_list

urlpatterns = [
    #path('', include('accueil.urls')), 
    path('', RedirectView.as_view(url='/accueil')), 
    path('accueil/', include('accueil.urls')),
    path('admin/', admin.site.urls),
    path('register/', register_request, name='register'),
    path('login/', login_request, name='login'),
    path('a_propos_de_nous/', include('accueil.urls')),
    path('nous_joindre/', include('accueil.urls')),
    path('logout/', logout_request, name='logout'),
    path('create/', userposts_create_view, name='userpost_create_view'),
    path('list/', userposts_list_view, name='userpost_list_view'),
    path('detail/(?P<url>\S+)/$', userposts_detail_view, name='userpost_detail_view'),
    path("conditions_d'utilisations/", include('accueil.urls')),
    path("a_lire/", include('accueil.urls')),
    path("profile_list/", profile_list, name="profile_list"),
    path("list_announce/", list_announce, name="list_announce"),
]
