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
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView

from django.contrib.auth import views as auth_views

from accueil import urls as accueil_urls
from accueil import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(accueil_urls)),
    
    path('', RedirectView.as_view(url='/accueil')), 

    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='login.html'), name='login'),
    path('register/', views.register_request, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='accueil'), name='logout'),

    path('accueil/details/<int:id>', views.details, name='details'),
    path('accueil/a_propos_de_nous/', views.aboutUs, name = 'aboutUs' ),
    path('accueil/nous_joindre/', views.nousJoindre, name = 'nousJoindre' ),
    path('accueil/conditions-d-utilisation/', views.conditionsUtilisations, name = 'conditionsUtilisations'),
    path("accueil/a_lire/", views.aLire, name = "a_lire"),

    path("profile_list/", views.profile_list, name="profile_list"),
    path("profile/<int:pk>", views.profile, name="profile"),
    path('dashboard/', views.dashboard, name= 'dashboard'),
    path('rechercher/', views.rechercher, name= 'rechercher'),

    path('accueil/', TemplateView.as_view(template_name='main.html'), name='accueil'), 

    path('profile/checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('rooms/<str:room>/', views.room, name='room'),
    path('getMessages/rooms/<str:room>/', views.getMessages, name='getMessages'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
