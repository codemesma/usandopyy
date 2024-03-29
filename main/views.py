from datetime import datetime
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.db.models import Count
from main import settings
from django.contrib import messages
from django.template import Context
from django.views.generic import ListView, DetailView
from django.urls import reverse
from .models import Tutorial,Download, Categoria, Tipo, Sobre
from django_blog_it.django_blog_it.models import Post, Canal, Equipa
from django.db.models import Q

from hitcount.views import HitCountDetailView

from mainsite.models import HomePageSettings
from news.models import Category, News

from django.http import HttpResponse
from django.views import View


from quiz.models import Quiz, Category, Progress, Sitting, Question
from essay.models import Essay_Question

from users.models import Profile


class AdsView(View):
    """Replace pub-0000000000000000 with your own publisher ID"""
    global line
    line  =  "google.com, pub-1810411345881098, DIRECT, f08c47fec0942fa0"
    def get(self, request, *args, **kwargs):
        return HttpResponse(line)



def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'404.html', data)


class Home(ListView):
    template_name = "theme/base.html"
    queryset = Categoria.objects.filter(is_active=True).order_by('id')
    context_object_name = "cat"

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
        context = super(Home, self).get_context_data(*args, **kwargs)

        results = self.get_home_page_post_list()
        context['hot_news'] = results[0]
        context['trending'] = results[6]
        context['editor_choice'] = results[7]

        context['tipo'] = Tipo.objects.all().order_by('id')
        context['canal'] = Canal.objects.all().order_by('id')
        context['equipa'] = Equipa.objects.all().order_by('id')
        context['sobre'] = Sobre.objects.all()

        context['tutorial'] = Tutorial.objects.filter(status='Published').order_by('-updated_on')[0:10]
        context['tutorial_'] = Tutorial.objects.filter(status='Published').order_by('-updated_on')[0:2]
        context['post'] = Post.objects.filter(status='Published').order_by('-updated_on')[0:10]
        context['post_banner'] = Post.objects.filter(status='Published').order_by('-updated_on')[0:4]
        context['categoria'] = Categoria.objects.all().order_by('name')
        context['categoria1'] = Categoria.objects.extra(select={'length':'Length(name)'}).order_by('length')

        context['users'] = Profile.objects.all()
        context['sitting_list'] = Sitting.objects.all().filter(complete=True).order_by('-id')[0:10]


        context.update({

            "description": settings.TUTORIAL_DESCRIPTION,
            "title": settings.TUTORIAL_TITLE,
            "keywords": settings.TUTORIAL_KEYWORDS,
            "author": settings.TUTORIAL_AUTHOR,
        })
        return context



class Tutoriais(ListView):
    template_name = "bases/tutorial.html"
    queryset = Categoria.objects.filter(is_active=True).order_by('id')
    context_object_name = "cat"

    def get_context_data(self, *args, **kwargs):
        context = super(Tutoriais, self).get_context_data(*args, **kwargs)

        context['tipo'] = Tipo.objects.all().order_by('id')
        context['canal'] = Canal.objects.all().order_by('id')
        context['equipa'] = Equipa.objects.all().order_by('id')
        context['sobre'] = Sobre.objects.all()

        context['tutorial'] = Tutorial.objects.filter(status='Published').order_by('-updated_on')[0:20]
        context['tipo'] = Tipo.objects.all().order_by('id')
        context['categoria'] = Categoria.objects.all().order_by('name')
        context['categoria1'] = Categoria.objects.extra(select={'length':'Length(name)'}).order_by('length')

        context.update({

            "description": settings.TUTORIAL_DESCRIPTION,
            "title": settings.TUTORIAL_TITLE,
            "keywords": settings.TUTORIAL_KEYWORDS,
            "author": settings.TUTORIAL_AUTHOR,
        })
        return context


class TutorialView(HitCountDetailView, DetailView):
    model = Tutorial
    context_object_name = 'tutorial'
    template_name = 'display/detalhe-view.html'
    query_pk_and_slug = True
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(TutorialView, self).get_context_data(**kwargs)
        context['sobre'] = Sobre.objects.all()
        context['tipo'] = Tipo.objects.all().order_by('id')
        context['categoria'] = Categoria.objects.all().order_by('name')
        context['categoria1'] = Categoria.objects.extra(select={'length':'Length(name)'}).order_by('length')

        tut = Tutorial.objects.all()
        context['tut'] = tut
        context['categoria'] = Categoria.objects.all()
        context['tipo'] = Tipo.objects.all().order_by('id')
        context['categoria'] = Categoria.objects.all().order_by('name')
        context['categoria1'] = Categoria.objects.extra(select={'length':'Length(name)'}).order_by('length')
        context.update({
            "og_image": self.object.featured_image,
            "description": self.object.meta_description if self.object.meta_description else "",
            "title": self.object.title,
            "keywords": self.object.keywords,
            "author": self.object.user,
            # "short_url": self.get_mini_url(self.request)
        })
        return context



class DownloadCode(HitCountDetailView, DetailView):
    model = Download
    context_object_name = 'tutorial'
    template_name = 'display/download.html'
    query_pk_and_slug = True
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(DownloadCode, self).get_context_data(**kwargs)
        context['sobre'] = Sobre.objects.all()
        context['tipo'] = Tipo.objects.all().order_by('id')
        context['categoria'] = Categoria.objects.all().order_by('name')
        context['categoria1'] = Categoria.objects.extra(select={'length':'Length(name)'}).order_by('length')
        context.update({
            "og_image": self.object.featured_image,
            "description": self.object.meta_description if self.object.meta_description else "",
            "title": self.object.nome,
            "keywords": self.object.keywords,
            # "short_url": self.get_mini_url(self.request)
        })
        return context


class SelectedCategoryView(ListView):
    model = Categoria
    template_name = "display/categoria.html"

    def get_queryset(self):

        self.tipo = get_object_or_404(Tipo, id=self.kwargs['id'])
        return Categoria.objects.filter(tipo=self.tipo, is_active=True,)


class CategoryView(DetailView):
    model = Categoria
    context_object_name = 'cat'
    template_name = 'bases/detalhe.html'
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        tut = Tutorial.objects.all()
        context['sobre'] = Sobre.objects.all()

        context['tut'] = tut
        context['tipo'] = Tipo.objects.all().order_by('id')
        context['categoria'] = Categoria.objects.all().order_by('name')
        context['categoria1'] = Categoria.objects.extra(select={'length':'Length(name)'}).order_by('length')
        context['categoria'] = Categoria.objects.all()
        context.update({
            "og_image": self.object.featured_image,
            "description": self.object.meta_description if self.object.meta_description else "",
            "title": self.object.name,
        })
        return context


class CookiePageView(ListView):
    template_name = 'bases/cookie.html'
    model = Sobre
    context_object_name = 'sobre'

    def get_context_data(self, *args, **kwargs):
        context = super(CookiePageView, self).get_context_data(*args, **kwargs)

        context['canal'] = Canal.objects.all().order_by('id')
        context['equipa'] = Equipa.objects.all().order_by('id')

        context['tutorial'] = Tutorial.objects.filter(
            status='Published')
        context['sobre'] = Sobre.objects.all()

        context['categoria'] = Categoria.objects.all()

        context.update({

            "description": settings.TUTORIAL_DESCRIPTION,
            "title": settings.TUTORIAL_TITLE,
            "keywords": settings.TUTORIAL_KEYWORDS,
            "author": settings.TUTORIAL_AUTHOR,
        })
        return context


class TermosPageView(ListView):
    template_name = 'bases/termos.html'
    model = Sobre
    context_object_name = 'sobre'

    def get_context_data(self, *args, **kwargs):
        context = super(TermosPageView, self).get_context_data(*args, **kwargs)

        context['canal'] = Canal.objects.all().order_by('id')
        context['equipa'] = Equipa.objects.all().order_by('id')

        context['tutorial'] = Tutorial.objects.filter(
            status='Published')
        context['sobre'] = Sobre.objects.all()

        context['categoria'] = Categoria.objects.all()

        context.update({

            "description": settings.TUTORIAL_DESCRIPTION,
            "title": settings.TUTORIAL_TITLE,
            "keywords": settings.TUTORIAL_KEYWORDS,
            "author": settings.TUTORIAL_AUTHOR,
        })
        return context


class Cookie(ListView):
    template_name = 'bases/cokie.html'
    model = Sobre
    context_object_name = 'sobre'

    def get_context_data(self, *args, **kwargs):
        context = super(Cookie, self).get_context_data(*args, **kwargs)

        context['canal'] = Canal.objects.all().order_by('id')
        context['equipa'] = Equipa.objects.all().order_by('id')

        context['tutorial'] = Tutorial.objects.filter(
            status='Published')
        context['sobre'] = Sobre.objects.all()

        context['categoria'] = Categoria.objects.all()

        context.update({

            "description": settings.TUTORIAL_DESCRIPTION,
            "title": settings.TUTORIAL_TITLE,
            "keywords": settings.TUTORIAL_KEYWORDS,
            "author": settings.TUTORIAL_AUTHOR,
        })
        return context


class SearchView(ListView):
    model = Tutorial
    template_name = "bases/search.html"

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Tutorial.objects.filter(
            Q(title__icontains=query) | Q(keywords__icontains=query)
        )
        return object_list

    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(*args, **kwargs)

        context['categoria'] = Categoria.objects.all()
        context['sobre'] = Sobre.objects.all()

        context.update({

            "description": settings.TUTORIAL_DESCRIPTION,
            "title": settings.TUTORIAL_TITLE,
            "keywords": settings.TUTORIAL_KEYWORDS,
            "author": settings.TUTORIAL_AUTHOR,
        })
        return context


class AboutPageView(ListView):
    template_name = 'bases/sobre.html'
    model = Sobre
    context_object_name = 'sobre'

    def get_context_data(self, *args, **kwargs):
        context = super(AboutPageView, self).get_context_data(*args, **kwargs)

        context['canal'] = Canal.objects.all().order_by('id')
        context['equipa'] = Equipa.objects.all().order_by('id')
        context['sobre'] = Sobre.objects.all()

        context['tutorial'] = Tutorial.objects.filter(
            status='Published')

        context['categoria'] = Categoria.objects.all()

        context.update({

            "description": settings.TUTORIAL_DESCRIPTION,
            "title": settings.TUTORIAL_TITLE,
            "keywords": settings.TUTORIAL_KEYWORDS,
            "author": settings.TUTORIAL_AUTHOR,
        })
        return context
