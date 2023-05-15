from django.urls import path
from . import views
from .views import profile_list, profile
from django.conf import settings
from django.conf.urls.static import static

app_name = "accueil"

urlpatterns = [
    path('details/<int:id>', views.details, name='details'),
    path("register", views.register_request, name="register"),
    path('a_propos_de_nous', views.aboutUs, name = 'aboutUs' ),
    path('nous_joindre', views.nousJoindre, name = 'nousJoindre' ),
    path('conditions-d-utilisation', views.conditionsUtilisations, name = 'conditionsUtilisations'),
    path("a_lire", views.aLire, name = "a_lire"),
    path("profile_list/", views.profile_list, name="profile_list"),
    path("profile/<int:pk>", views.profile, name="profile"),
    path('dashboard', views.dashboard, name= 'dashboard'),
    path('rechercher', views.rechercher, name= 'rechercher'),
    path('rooms/<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
