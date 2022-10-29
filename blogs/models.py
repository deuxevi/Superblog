from django.db import models
from django.utils.text import slugify
from django.urls import reverse

from utilisateur.models import User



class Themes(models.Model):
	theme=models.CharField(max_length=50, verbose_name='theme de l\'article')


class Articles(models.Model):
	title=models.CharField(max_length=100, verbose_name='titre de l\'article')
	contenu=models.TextField(verbose_name='Contenu')
	author=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	published=models.BooleanField(default=False)
	date_pub=models.DateTimeField(auto_now_add=True)
	date_mod=models.DateTimeField(auto_now=True)
	theme=models.ForeignKey(Themes, on_delete=models.SET_NULL, null=True, blank=True)
	slug = models.SlugField(max_length=255, blank=True)

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

class Likes(models.Model):
	status=models.BooleanField(verbose_name='Like')
	article=models.ForeignKey(Articles, on_delete=models.CASCADE)
	user=models.ForeignKey(User, on_delete=models.CASCADE)

class Comments(models.Model):
	article=models.ForeignKey(Articles, on_delete=models.CASCADE)
	contenu=models.TextField()
	internaute=models.ForeignKey(User,on_delete=models.CASCADE)
	date=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.contenu

class Enregistrements(models.Model):
	status=models.BooleanField(verbose_name='Save')
	article=models.ForeignKey(Articles, on_delete=models.CASCADE)
	owner=models.ForeignKey(User, on_delete=models.CASCADE)


