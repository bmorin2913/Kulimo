from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  password = models.CharField(max_length=255, null=True)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"

User= settings.AUTH_USER_MODEL

class UserPost(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.CharField(max_length=500)
    content= models.TextField()
    date_published= models.DateField(default=timezone.now)
    url= models.SlugField(max_length=500, unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.url= slugify(self.title)
        super(UserPost, self).save(*args, **kwargs)    


