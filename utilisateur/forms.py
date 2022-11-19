from django import forms
from django.forms import ModelForm
from utilisateur.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
	username = forms.CharField(label="Nom d'utilisateur")
	password = forms.CharField(widget=forms.PasswordInput, label='Mot de passe')

class InscriptionForm(UserCreationForm):
		class Meta(UserCreationForm.Meta):
			model = User
			fields = ('profile_photo', 'username', 'email', 'first_name', 'last_name', 'role')






	
	
