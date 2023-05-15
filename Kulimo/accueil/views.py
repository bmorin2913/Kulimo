from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader, RequestContext
from .models import Member, UserPost, Profile, Room, Message
from django.shortcuts import  render, redirect, get_object_or_404
from .forms import NewUserForm, UserPostForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm



def accueil(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))

def register_request(request):
	form = NewUserForm(request.POST)
	if request.method == "POST":
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect('/accueil/')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect('/accueil/')
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def aboutUs(request):
	template = loader.get_template('a_propos_de_nous.html')
	return HttpResponse(template.render())

def nousJoindre(resquest):
	template = loader.get_template('nous_joindre.html')
	return HttpResponse(template.render())

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect('/accueil/')


def conditionsUtilisations(request):
	template = loader.get_template('conditions_utilisations.html')
	return HttpResponse(template.render())


def aLire(requst):
	template = loader.get_template('a_lire.html')
	return HttpResponse(template.render())

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "profile_list.html", {"profiles": profiles})

def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    profile_string = profile.user.username
    username = request.user.username
    roomname = username + profile_string
    return render(request, "profile.html", {"profile": profile, 'username': username, 'roomname': roomname, 'profile_string': profile_string})

def dashboard(request):
    form = UserPostForm(request.POST or None)
    if request.method == "POST":
        print('test')
        form = UserPostForm(request.POST, request.FILES)
        if form.is_valid():
            print('form saved')
            UserPost = form.save(commit=False)
            UserPost.user = request.user
            UserPost.save()
            img_object = form.instance
            return render(request, "dashboard.html", {"form": form, 'img_obj': img_object})
        else:
          form = UserPostForm()

    return render(request, "dashboard.html", {"form": form})

def rechercher(request):
	if request.method == "POST":
		searched = request.POST['searched']
		posts = UserPost.objects.filter(title__contains=searched)

		return render(request, 'recherche.html', {'searched':searched, 'posts':posts})
	else:
		return render(request, 'recherche.html', {})
	
def room(request, room):
	username = request.GET.get('username')
	room_details = Room.objects.get(name=room)
	return render(request, 'room.html', {'username': username, 'room': room, 'room_details': room_details})

def checkview(request):
	room = request.POST['room_name']
	username = request.POST['username']
	profile = request.POST['profile']
	check = Room.objects.filter(name=room).exists()
	check2 = (Room.objects.filter(name=profile+username))
	if check:
		return redirect('/rooms/'+room+'/?username='+username)
	elif check2:
		return redirect('/rooms/'+ profile + username+'/?username='+username)
	else:
		new_room = Room.objects.create(name=room)
		new_room.save()
		return redirect('/rooms/'+room+'/?username='+username)
	
def send(request):
	message = request.POST['message']
	username = request.POST['username']
	room_id = request.POST['room_id']

	new_message = Message.objects.create(value=message, user=username, room=room_id)
	new_message.save()
	return HttpResponse('Message envoyé avec succès')

def getMessages(request, room):
	room_details = Room.objects.get(name=room)

	messages = Message.objects.filter(room=room_details.id)
	return JsonResponse({"messages":list(messages.values())})

