from django import forms
from django.forms import ModelForm
from utilisateur.models import User
from blogs.models import *



class ArticlesForm(ModelForm):
	class Meta():
		model = Articles
		fields=('title', 'contenu', 'theme')


class CommentsForm(ModelForm):
	class Meta():
		model=Comments
		fields=('contenu')