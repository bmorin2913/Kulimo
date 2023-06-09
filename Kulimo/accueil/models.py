from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.sessions.models import Session
from django.contrib.auth.signals import user_logged_in

# Fichier qui définit les différents modèles utilisé dans notre application

# Classe importée de Django qui définit les utilisateurs
User= settings.AUTH_USER_MODEL

# Classe qui définit les publications des utiliateurs
class UserPost(models.Model):
    user= models.ForeignKey(User, related_name="userposts", on_delete=models.DO_NOTHING)
    title= models.CharField(max_length=100)
    content= models.TextField()
    date_published= models.DateTimeField(auto_now_add=True)
    image= models.ImageField(upload_to='images')
    url= models.SlugField(max_length=500, unique=True, blank=True, editable=False)
    def save(self, *args, **kwargs):
        self.url= slugify(self.title)
        super(UserPost, self).save(*args, **kwargs)    

# Classe qui définit la page profile des utilisateurs
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

# Classe qui définit une salle de messagerie entre deux utilisateurs
class Room(models.Model):
   name = models.CharField(max_length=1000)

# Classe qui défini un message envoyé par un utilisateur
class Message(models.Model):
   value = models.CharField(max_length=1000)
   date = models.DateTimeField(auto_now_add=True)
   user = models.CharField(max_length=1000)
   room = models.CharField(max_length=1000000)

# Méthode qui crée automatiquement un profil associé à un utilisateur lorsque ce dernier est crée
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()




