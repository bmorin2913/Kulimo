from django.urls import path
from . import views
from .views import profile_list, profile
from django.conf import settings
from django.conf.urls.static import static

app_name = "accueil"

urlpatterns = [
    path('', views.main, name='main'),
    path('accueil/', views.accueil, name='accueil'),
    path('details/<int:id>', views.details, name='details'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path('a_propos_de_nous', views.aboutUs, name = 'aboutUs' ),
    path('nous_joindre', views.nousJoindre, name = 'nousJoindre' ),
    path('logout', views.logout_request, name= 'logout'),
    path('conditions-d-utilisation', views.conditionsUtilisations, name = 'conditionsUtilisations'),
    path("a_lire", views.aLire, name = "a_lire"),
    path("profile_list/", views.profile_list, name="profile_list"),
    path("profile/<int:pk>", views.profile, name="profile"),
    path('dashboard', views.dashboard, name= 'dashboard')
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
