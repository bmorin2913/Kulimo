from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader, RequestContext
from .models import UserPost, Profile, Room, Message
from django.shortcuts import  render, redirect, get_object_or_404
from .forms import NewUserForm, UserPostForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Fichier qui définit la logique en backend des différentes pages de notre site

# La page d'accueil de notre site
def accueil(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

# Un autre moyen d'accéder à la page d'accueil
def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

# La page pour créer un compte
def register_request(request):
	form = NewUserForm(request.POST) # On utilise le formulaire de création de publication
	if request.method == "POST":
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('/accueil/')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form}) # On affiche la template HTML de la page

# La page pour se connecter
def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None: # Si l'utilisateur est trouvé dans la base de donnée
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('/accueil/') # On redirige à l'accueil
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form}) # On affiche la template HTML de la page

# La page 'à propos de nous'
def aboutUs(request):
	template = loader.get_template('a_propos_de_nous.html')
	return HttpResponse(template.render()) # On affiche la template HTML de la page

# La page 'nous joindre'
def nousJoindre(resquest):
	template = loader.get_template('nous_joindre.html')
	return HttpResponse(template.render())

# La méthode qui permet de se déconnecter et redirige à l'accueil
def logout_request(request):
	logout(request)
	messages.info(request, "Vous vous êtes déconnecté avec succès") 
	return redirect('/accueil/')

# La page 'conditions d'utilisation'
def conditionsUtilisations(request):
	template = loader.get_template('conditions_utilisations.html')
	return HttpResponse(template.render()) # On affiche la template HTML de la page

# La page 'à lire'
def aLire(request):
	template = loader.get_template('a_lire.html')
	return HttpResponse(template.render()) # On affiche la template HTML de la page

# La liste de profils
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "profile_list.html", {"profiles": profiles}) # On affiche la template HTML de la page

# La page qui affiche le profil d'un utilisateur
def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    profile_string = profile.user.username
    username = request.user.username
    roomname = username + profile_string
    return render(request, "profile.html", {"profile": profile, 'username': username, 'roomname': roomname, 'profile_string': profile_string}) # On affiche la template HTML de la page

# La page pour créer une publication
def dashboard(request):
    form = UserPostForm(request.POST or None)
    if request.method == "POST":
        form = UserPostForm(request.POST, request.FILES)
        if form.is_valid():
            UserPost = form.save(commit=False)
            UserPost.user = request.user
            UserPost.save()
            img_object = form.instance
            return render(request, "dashboard.html", {"form": form, 'img_obj': img_object}) # On affiche la template HTML de la page
        else:
          form = UserPostForm()

    return render(request, "dashboard.html", {"form": form}) # On affiche la template HTML de la page

# La page pour rechercher des publications
def rechercher(request):
	if request.method == "POST":
		searched = request.POST['searched']
		posts = UserPost.objects.filter(title__contains=searched)

		return render(request, 'recherche.html', {'searched':searched, 'posts':posts})
	else:
		return render(request, 'recherche.html', {}) # On affiche la template HTML de la page

# La salle de messagerie	
def room(request, room):
	username = request.GET.get('username')
	room_details = Room.objects.get(name=room)
	return render(request, 'room.html', {'username': username, 'room': room, 'room_details': room_details}) # On affiche la template HTML de la page

# Méthode qui permet de créer la salle de messagerie où d'y accéder avant de l'afficher
def checkview(request):
	room = request.POST['room_name']
	username = request.POST['username']
	profile = request.POST['profile']
	check = Room.objects.filter(name=room).exists() 
	check2 = (Room.objects.filter(name=profile+username))
	if check: # On vérifie s'il existe déjà une salle entre les deux utilisateurs
		return redirect('/rooms/'+room+'/?username='+username)
	elif check2: # On vérifie s'il existe déjà une salle entre les deux utilisateurs
		return redirect('/rooms/'+ profile + username+'/?username='+username)
	else: # S'il n'a pas déjà de salle, on en crée une
		new_room = Room.objects.create(name=room)
		new_room.save()
		return redirect('/rooms/'+room+'/?username='+username)

# Méthode qui permet d'envoyer un message	
def send(request):
	message = request.POST['message']
	username = request.POST['username']
	room_id = request.POST['room_id']

	new_message = Message.objects.create(value=message, user=username, room=room_id)
	new_message.save()
	return HttpResponse('Message envoyé avec succès')

# Méthode qui permet d'accéder à tous les messages d'une salle
def getMessages(request, room):
	room_details = Room.objects.get(name=room)

	messages = Message.objects.filter(room=room_details.id)
	return JsonResponse({"messages":list(messages.values())})

