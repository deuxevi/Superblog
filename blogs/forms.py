from django.forms import ModelForm, TextInput
from blogs.models import Comments


class CommentForm(ModelForm):
	class Meta:
		model = Comments
		fields = ['contenu']
		widget = {'contenu': TextInput(attrs={'id':"comment",
		 'rows':"4",
		  'class':"px-0 w-full text-sm text-gray-900 bg-white border-0 dark:bg-gray-800 focus:ring-0 dark:text-white dark:placeholder-gray-400",
		   'placeholder':"Write a comment...",
		    'required':""})}

