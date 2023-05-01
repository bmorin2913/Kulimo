from django.urls import path
from . import views
from .views import profile_list, profile

app_name = "accueil"

urlpatterns = [
    path('', views.main, name='main'),
    path('accueil/', views.accueil, name='accueil'),
    path('details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path('a_propos_de_nous', views.aboutUs, name = 'aboutUs' ),
    path('nous_joindre', views.nousJoindre, name = 'nousJoindre' ),
    path('logout', views.logout_request, name= 'logout'),
    path('create', views.userposts_create_view, name= 'userpost_create_view'),
    path('list', views.userposts_list_view, name= 'userpost_list_view'),
    path('detail', views.userposts_detail_view, name= 'userpost_detail_view'),
    path('conditions-d-utilisation', views.conditionsUtilisations, name = 'conditionsUtilisations'),
    path("a_lire", views.aLire, name = "a_lire"),
    path("profile_list/", views.profile_list, name="profile_list"),
    path("profile/<int:pk>", views.profile, name="profile"),
    path("list_announce/", views.list_announce, name="list_announce"),
]
