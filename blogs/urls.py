from django.urls import path
from blogs.views import *

app_name = "blog"

urlpatterns = [
	path('', BlogHome.as_view(), name="home"),
	path('search/', ArticleSearch.as_view(), name="search"),
	path('mes-articles/', BlogArticles.as_view(), name='mesArticles'),
	path('photo/view/', photo_view, name='photo_view'),
	path('brouillons/', Brouillons.as_view(), name='brouillons'),
	path('create/', CreateArticle.as_view(), name="add"),
	path('photo/upload/', photo_upload, name='photo_upload'),
	path('addcomment/', AddComment.as_view(), name="comment"),
	path('<str:slug>/', DetailArticle.as_view(), name="detail"),
	path('edit/<str:slug>', EditArticle.as_view(), name="edit"),
	path('supprimer/<str:slug>', DeleteArticle.as_view(), name="delete"),
	path('like/<str:slug>', article_like, name="like"),
	path('save/<str:slug>', article_save, name="save"),

	
]