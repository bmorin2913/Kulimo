from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member, UserPost
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

#create view
def userposts_create_view(request):
    form= UserPostForm(request.POST or None)
    

    if request.method == "POST":
        if form.is_valid():
            form.save()
        return redirect('/accueil/')

    
    
    context= {'form': form,
              }
    
    return render(request, 'userposts-create-view.html', context)

#list view
def userposts_list_view(request):

    allposts= UserPost.objects.all()
    
    context= {'allposts': allposts,
              }
    
    return render(request, 'userposts-list-view.html', context)

#detail view
def userposts_detail_view(request, url=None):

    post= get_object_or_404(UserPost, url=url)


    
    
    context= {'post': post,
              }
    
    return render(request, 'userposts-detail-view.html', context)
	

def conditionsUtilisations(request):
	template = loader.get_template('conditions_utilisations.html')
	return HttpResponse(template.render())


def aLire(requst):
	template = loader.get_template('a_lire.html')
<<<<<<< Updated upstream
	return HttpResponse(template.render())
=======
	return HttpResponse(template.render())

def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "profile_list.html", {"profiles": profiles})

def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    return render(request, "profile.html", {"profile": profile})
>>>>>>> Stashed changes
