from django.shortcuts import render 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin 
from hitcount.views import HitCountDetailView

from .models import Book, Order, Book_Category


from main.models import Tutorial, Categoria, Tipo, Sobre
from django_blog_it.django_blog_it.models import Post, Canal, Equipa

from mainsite.models import HomePageSettings
from news.models import Category, News




from django.urls import reverse_lazy
from django.db.models import Q # for search method
from django.http import JsonResponse
import json



class BooksListView(ListView):
    model = Book
    template_name = 'list.html'
    
    def get_home_page_post_list(self):
        home_page_settings = HomePageSettings.objects.last()
        news_list = News.objects.all()
        post_catalog_one = news_list.filter(category=home_page_settings.post_catalog_one).order_by('-id')[:3]
        post_catalog_two = news_list.filter(category=home_page_settings.post_catalog_two).order_by('-id')[:2]
        post_catalog_three = news_list.filter(category=home_page_settings.post_catalog_three).order_by('-id')[:2]
        post_catalog_four = news_list.filter(category=home_page_settings.post_catalog_four).order_by('-id')[:3]
        post_catalog_five = news_list.filter(category=home_page_settings.post_catalog_five).order_by('-id')[:2]
        return (home_page_settings.hot_news, post_catalog_one, post_catalog_two, post_catalog_three,
                post_catalog_four, post_catalog_five, home_page_settings.trending, home_page_settings.editor_choice)
    
    def get_context_data(self, *args, **kwargs):
        context = super(BooksListView, self).get_context_data(*args, **kwargs)
        results = self.get_home_page_post_list()
        context['hot_news'] = results[0]
        context['trending'] = results[6]
        context['editor_choice'] = results[7]

        context['tipo'] = Tipo.objects.all().order_by('id')
        context['categoria1'] = Categoria.objects.extra(select={'length':'Length(name)'}).order_by('length')
        context['canal'] = Canal.objects.all().order_by('id')
        context['equipa'] = Equipa.objects.all().order_by('id')
        context['sobre'] = Sobre.objects.all()
        
        context['book_categoria'] = Book_Category.objects.all()
        
        return context


class BooksCategoryView(DetailView):
    model = Book_Category
    context_object_name = 'cat'
    template_name = 'book_cat.html'
    query_pk_and_slug = True
    
    def get_home_page_post_list(self):
        home_page_settings = HomePageSettings.objects.last()
        news_list = News.objects.all()
        post_catalog_one = news_list.filter(category=home_page_settings.post_catalog_one).order_by('-id')[:3]
        post_catalog_two = news_list.filter(category=home_page_settings.post_catalog_two).order_by('-id')[:2]
        post_catalog_three = news_list.filter(category=home_page_settings.post_catalog_three).order_by('-id')[:2]
        post_catalog_four = news_list.filter(category=home_page_settings.post_catalog_four).order_by('-id')[:3]
        post_catalog_five = news_list.filter(category=home_page_settings.post_catalog_five).order_by('-id')[:2]
        return (home_page_settings.hot_news, post_catalog_one, post_catalog_two, post_catalog_three,
                post_catalog_four, post_catalog_five, home_page_settings.trending, home_page_settings.editor_choice)
    
    def get_context_data(self, *args, **kwargs):
        context = super(BooksCategoryView, self).get_context_data(*args, **kwargs)
        results = self.get_home_page_post_list()
        
        context['book'] = Book.objects.all()
        
        context['hot_news'] = results[0]
        context['trending'] = results[6]
        context['editor_choice'] = results[7]

        context['tipo'] = Tipo.objects.all().order_by('id')
        context['categoria1'] = Categoria.objects.extra(select={'length':'Length(name)'}).order_by('length')
        context['canal'] = Canal.objects.all().order_by('id')
        context['equipa'] = Equipa.objects.all().order_by('id')
        context['sobre'] = Sobre.objects.all()
        
        context['book_categoria'] = Book_Category.objects.all()
        
        return context


class BooksDetailView(DetailView):
    model = Book
    template_name = 'detail.html'
    
    def get_home_page_post_list(self):
        home_page_settings = HomePageSettings.objects.last()
        news_list = News.objects.all()
        post_catalog_one = news_list.filter(category=home_page_settings.post_catalog_one).order_by('-id')[:3]
        post_catalog_two = news_list.filter(category=home_page_settings.post_catalog_two).order_by('-id')[:2]
        post_catalog_three = news_list.filter(category=home_page_settings.post_catalog_three).order_by('-id')[:2]
        post_catalog_four = news_list.filter(category=home_page_settings.post_catalog_four).order_by('-id')[:3]
        post_catalog_five = news_list.filter(category=home_page_settings.post_catalog_five).order_by('-id')[:2]
        return (home_page_settings.hot_news, post_catalog_one, post_catalog_two, post_catalog_three,
                post_catalog_four, post_catalog_five, home_page_settings.trending, home_page_settings.editor_choice)
    
    def get_context_data(self, *args, **kwargs):
        context = super(BooksDetailView, self).get_context_data(*args, **kwargs)
        results = self.get_home_page_post_list()
        context['hot_news'] = results[0]
        context['trending'] = results[6]
        context['editor_choice'] = results[7]

        context['tipo'] = Tipo.objects.all().order_by('id')
        context['categoria1'] = Categoria.objects.extra(select={'length':'Length(name)'}).order_by('length')
        context['canal'] = Canal.objects.all().order_by('id')
        context['equipa'] = Equipa.objects.all().order_by('id')
        context['sobre'] = Sobre.objects.all()
        return context


class SearchResultsListView(ListView):
    model = Book
    template_name = 'search_results.html'
    
    def get_home_page_post_list(self):
        home_page_settings = HomePageSettings.objects.last()
        news_list = News.objects.all()
        post_catalog_one = news_list.filter(category=home_page_settings.post_catalog_one).order_by('-id')[:3]
        post_catalog_two = news_list.filter(category=home_page_settings.post_catalog_two).order_by('-id')[:2]
        post_catalog_three = news_list.filter(category=home_page_settings.post_catalog_three).order_by('-id')[:2]
        post_catalog_four = news_list.filter(category=home_page_settings.post_catalog_four).order_by('-id')[:3]
        post_catalog_five = news_list.filter(category=home_page_settings.post_catalog_five).order_by('-id')[:2]
        return (home_page_settings.hot_news, post_catalog_one, post_catalog_two, post_catalog_three,
                post_catalog_four, post_catalog_five, home_page_settings.trending, home_page_settings.editor_choice)
    
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        return Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
    
    def get_context_data(self, *args, **kwargs):
        context = super(SearchResultsListView, self).get_context_data(*args, **kwargs)
        results = self.get_home_page_post_list()
        context['hot_news'] = results[0]
        context['trending'] = results[6]
        context['editor_choice'] = results[7]

        context['tipo'] = Tipo.objects.all().order_by('id')
        context['categoria1'] = Categoria.objects.extra(select={'length':'Length(name)'}).order_by('length')
        context['canal'] = Canal.objects.all().order_by('id')
        context['equipa'] = Equipa.objects.all().order_by('id')
        context['sobre'] = Sobre.objects.all()
        
        return context

class BookCheckoutView(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'checkout.html'
    login_url     = 'login'


def paymentComplete(request):
	body = json.loads(request.body)
	print('BODY:', body)
	product = Book.objects.get(id=body['productId'])
	Order.objects.create(
		product=product
	)
	return JsonResponse('Payment completed!', safe=False)

