from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Member, UserPost

# Register your models here.

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname")

admin.site.register(UserPost)

