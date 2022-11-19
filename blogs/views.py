from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
import operator
from functools import reduce
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

import utilisateur.models as user
import blogs.models as blog
import blogs.forms as forms


class BlogHome(ListView):
	model = blog.Articles
	context_object_name = "articles"

	def get_queryset(self):
		queryset = super().get_queryset()
		if self.request.user.is_authenticated and self.request.user.role == 'Créateur':
			return queryset.filter

		return queryset.filter(published=True)

class BlogArticles(ListView):
	model = blog.Articles
	context_object_name = "articles"

	def get_queryset(self):
		queryset = super().get_queryset()

		return queryset.filter(author=self.request.user).filter(published=True)

class Brouillons(ListView):
	model = blog.Articles
	context_object_name = "articles"

	def get_queryset(self):
		queryset = super().get_queryset()

		return queryset.filter(author=self.request.user).filter(published=False)

class Enregistrements(ListView):
	model = blog.Articles
	context_object_name = "articles"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['articles'] = self.request.user.article_save.all()

		return context
			

class CreateArticle(LoginRequiredMixin, CreateView):
	model = blog.Articles
	template_name = "blogs/article_create.html"
	fields = ["image", "title", 'theme', 'contenu', 'tags', 'published']


	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)



class EditArticle(UpdateView):
	model = blog.Articles
	template_name = "blogs/article_edit.html"
	fields = ["image", "title", "theme", "contenu", "published"]


class DetailArticle(DetailView):
	model = blog.Articles
	context_object_name = "article"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		article = blog.Articles.objects.get(slug=self.kwargs['slug'])
		liked = False
		saved = False
		if article.likes.filter(id=self.request.user.id).exists():
			liked = True
		if article.enregistrements.filter(id=self.request.user.id).exists():
			saved = True
		context["commentForm"] = forms.CommentForm()
		context["saved"] = saved
		context["comments"] = blog.Comments.objects.filter(article=self.object)
		context["likes"] =article.nb_likes()
		context["liked"] = liked
		return context


	def post(self,request, slug):
		form = forms.CommentForm(request.POST)
		if form.is_valid():
			form.instance.internaute = self.request.user
			form.instance.article=blog.Articles.objects.get(slug=slug)
			form.save()

			return HttpResponseRedirect(reverse('blog:detail', args=[str(slug)]))

class DeleteArticle(DeleteView):
	model = blog.Articles
	succes_url = reverse_lazy('blog:home')



class AddComment(LoginRequiredMixin, CreateView):
	model = blog.Comments
	template_name = "blogs/articles_detail.html"
	fields = ["contenu"]

	def form_valid(self, form):
		form.instance.internaute = self.request.user
		#form.instance.article = blog.Comments.objects.get(slug=)
		return super().form_valid(form)

	



class ArticleSearch(ListView):
    model = blog.Articles
    context_object_name = "articles"
    template_name = "articles_list.html"
    paginate_by = 10

    def get_queryset(self):
        result = super(ArticleSearch, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            query_list = query.split()
            result = result.filter(
                reduce(operator.and_,
                       (Q(title__icontains=q) for q in query_list)) |
                reduce(operator.and_,
                       (Q(contenu__icontains=q) for q in query_list))
            )

        return result




def article_like(request, slug):
	article = blog.Articles.objects.get(slug=slug)
	if article.likes.filter(id=request.user.id).exists():
		article.likes.remove(request.user)
	else:
		article.likes.add(request.user)

	return HttpResponseRedirect(reverse('blog:detail', args=[str(slug)]))


def article_save(request, slug):
	article = blog.Articles.objects.get(slug=slug)
	if article.enregistrements.filter(id=request.user.id).exists():
		article.enregistrements.remove(request.user)
	else:
		article.enregistrements.add(request.user)

	return HttpResponseRedirect(reverse('blog:detail', args=[str(slug)]))