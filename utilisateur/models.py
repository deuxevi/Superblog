from django.contrib.auth.models import AbstractUser
from django.db import models


BLOGGEUR = 'BLOGGEUR'
INTERNAUTE = 'INTERNAUTE'
ROLE_CHOICES = [(BLOGGEUR, 'Créateur'), (INTERNAUTE, 'Abonné')]

class User(AbstractUser):
	#profile_photo = models.ImageField(verbose_name='Photo de profil')
	role = models.CharField(max_length=10, choices=ROLE_CHOICES, verbose_name='Rôle')

	def __str__(self):
		return self.username

	def is_createur(self):
		return self.role == 'Créateur'


	
