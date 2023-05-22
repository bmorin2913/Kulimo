from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import UserPost, Profile, Room, Message

# Classe qui permet de gérer le site sur la page /admin

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname")

admin.site.register(UserPost)
admin.site.register(Profile)
admin.site.register(Room)
admin.site.register(Message)


