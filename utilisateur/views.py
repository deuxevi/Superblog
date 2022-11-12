from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.generic import UpdateView

from . import forms
from . import models

def login_page(request):
	form = forms.LoginForm()
	message = ''
	if request.method == 'POST':
		form = forms.LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username = form.cleaned_data['username'],password = form.cleaned_data['password'])
			if user is None:
				message = 'Identifiants invalides'
			else:
				login(request,user)
				message = f'Bonjour {user.username}! Vous etes connecte.'
				return redirect('blog:home')

	return render (request, 'utilisateur/login.html', {'form':form, 'message':message})


def inscription(request):
	if request.method == 'POST':
		form = forms.InscriptionForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)
			return redirect('blog:home')
	else:
		form = forms.InscriptionForm()
	return render(request,'utilisateur/inscription.html', {'form' : form})




def logout_user(request):
	logout(request)
	return redirect('blog:home')

def profil(request):
	return render (request, 'utilisateur/profil.html')

class UpdateUser(UpdateView):
	model = models.User
	template_name = "utilisateur/user_edit.html"
	fields = ['username', 'email', 'first_name', 'last_name']

class UpdatePassWord(UpdateView):
	model = models.User
	template_name = "utilisateur/user_edit"
	fields = ['password']