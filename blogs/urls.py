from django.urls import path
from blogs.views import *

app_name = "blog"

urlpatterns = [
	path('', BlogHome.as_view(), name="home"),
	path('create/', CreateArticle.as_view(), name="add"),
	path('addcomment/', AddComment.as_view(), name="comment"),
	path('<str:slug>/', DetailArticle.as_view(), name="detail"),
	path('edit/<str:slug>', EditArticle.as_view(), name="edit"),
	path('supprimer/<str:slug>', DeleteArticle.as_view(), name="delete"),
	
]