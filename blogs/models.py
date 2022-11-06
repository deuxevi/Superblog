from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings

from utilisateur.models import User



class Photo(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length=128, blank=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

class Themes(models.Model):
	theme=models.CharField(max_length=50, verbose_name='theme de l\'article')

	def __str__(self):
		return self.theme


class Articles(models.Model):
	photo = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
	title=models.CharField(max_length=100, verbose_name='titre de l\'article')
	contenu=models.TextField(verbose_name='Contenu')
	author=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	published=models.BooleanField(default=False)
	date_pub=models.DateTimeField(auto_now_add=True)
	date_mod=models.DateTimeField(auto_now=True)
	theme=models.ForeignKey(Themes, on_delete=models.SET_NULL, null=True, blank=True)
	slug = models.SlugField(max_length=255, blank=True)
	likes = models.ManyToManyField(User, related_name='article_like')
	enregistrements = models.ManyToManyField(User, related_name='article_save')


	class Meta:
		ordering = ['-date_pub']
		verbose_name = "Article"

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.author.username + "_" + self.title)

		super().save(*args, **kwargs)


	def get_absolute_url(self):
		return reverse("blog:home")

	def nb_likes(self):
		return self.likes.count()

"""class Likes(models.Model):
	status=models.BooleanField(verbose_name='Like')
	article=models.ForeignKey(Articles, on_delete=models.CASCADE)
	user=models.ForeignKey(User, on_delete=models.CASCADE)"""

class Comments(models.Model):
	article=models.ForeignKey(Articles, on_delete=models.CASCADE)
	contenu=models.TextField()
	internaute=models.ForeignKey(User,on_delete=models.CASCADE)
	date=models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-date']
		verbose_name = "Commentaire"

	def __str__(self):
		return self.contenu

"""class Enregistrements(models.Model):
	status=models.BooleanField(verbose_name='Save')
	article=models.ForeignKey(Articles, on_delete=models.CASCADE)
	owner=models.ForeignKey(User, on_delete=models.CASCADE)"""


