from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from .models import Member, UserPost, Profile
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

def aboutUs(request):
	template = loader.get_template('a_propos_de_nous.html')
	return HttpResponse(template.render())

def nousJoindre(resquest):
	template = loader.get_template('nous_joindre.html')
	return HttpResponse(template.render())

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
    return render(request, "profile.html", {"profile": profile})

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