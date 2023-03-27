from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('accueil/', views.accueil, name='accueil'),
    path('details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login")
]
