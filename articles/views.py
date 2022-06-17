from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from articles.models import Article
from .models import Article


class ArticleListView(LoginRequiredMixin, ListView):
    template_name = "articles/list.html"
    model= Article
    success_url = reverse_lazy ("detail") 
    


class NewsArticleListView(ArticleListView):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Article.objects.filter(section=1).order_by('created_on').reverse()
        context["section"] = "News"
        return context

class PoliticsArticleListView(ArticleListView):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Article.objects.filter(section=2).order_by('created_on').reverse()
        context["section"] = "Politics"
        return context

class GoGamecocksArticleListView(ArticleListView):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Article.objects.filter(section=3).order_by('created_on').reverse()
        context["section"] = "GoGamecocks"
        return context       

class PersonalFinanceArticleListView(ArticleListView):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Article.objects.filter(section=4).order_by('created_on').reverse()
        context["section"] = "PersonalFinance"
        return context
        
class SportsArticleListView(ArticleListView):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Article.objects.filter(section=5).order_by('created_on').reverse()
        context["section"] = "Sports"
        return context

class ArticleDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    template_name = "articles/detail.html"
    model= Article  

    def test_func(self):
        article = self.get_object()
        return article.author == self.request.user  

class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = "articles/new.html"
    model= Article
    fields = ["title", "section", "body", "author" ] 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.role.id > 1   

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "articles/edit.html"
    model= Article
    fields = ["title", "section", "body", "author"]
    
    def test_func(self):
        if self.request.user.role.id > 1:
            article = self.get_object()
            return article.author == self.request.user
        return False

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "articles/delete.html"
    model= Article
    success_url = reverse_lazy ("home")  

    def test_func(self):
        if self.request.user.role.id > 1:
            article = self.get_object()
            return article.author == self.request.user  
        return False     

# Create your views here.
