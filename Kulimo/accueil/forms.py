from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserPost


# Classe qui définit les différents formulaires que l'utilisateur peut remplir


# Le formulaire pour la création d'un compte
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)


	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
	
# Le formulaire pour la création d'une publication
class UserPostForm(forms.ModelForm):
	
    class Meta:
        model= UserPost
        fields= ["title", "content", "image"]
        exclude = ("user", )
