from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

import utilisateur.models as user
import blogs.models as blog


class BlogHome(ListView):
	model = blog.Articles
	context_object_name = "articles"

	def get_queryset(self):
		queryset = super().get_queryset()
		if self.request.user.is_authenticated and self.request.user.role == 'Créateur':
			return queryset

		return queryset.filter(published=True)

class CreateArticle(CreateView):
	model = blog.Articles
	template_name = "blogs/article_create.html"
	fields = ["title", 'theme', 'contenu', 'published'] 



class EditArticle(UpdateView):
	model = blog.Articles
	template_name = "blogs/article_edit.html"
	fields = ["title", "theme", "contenu"]


class DetailArticle(DetailView):
	model = blog.Articles
	context_object_name = "article"


class DeleteArticle(DeleteView):
	model = blog.Articles
	succes_url = reverse_lazy('blog:home')



class AddComment(CreateView):
	model = blog.Comments
	template_name = "blogs/comment_add.html"
	fields = ["contenu"]