from django.forms import ModelForm
from blogs.models import Comments, Enregistrements, Likes


class CommentForm(ModelForm):
	class Meta:
		model = Comments
		fields = ['contenu']


class EnregistrementForm(ModelForm):
	class Meta:
		model = Enregistrements
		fields=['status']

class LikeForm(ModelForm):
	class Meta:
		model = Likes
		fields = ['status']