from django.shortcuts import render, get_object_or_404
from .cookies import cookie_to_template
from django.views.generic import ListView, DetailView
from .models import *


class AllArticlesListView(ListView):
    model = Article
    ordering = ['-datetime']
    paginate_by = 20
    template_name = 'htp_app/list_view.html'
    context_object_name = 'all_articles'

    def get_context_data(self, **kwargs):
        request = self.request
        context = super().get_context_data(**kwargs)
        cookies = cookie_to_template(request)
        context.update(cookies)
        return context


class ArticleDetailView(DetailView):
    template_name = 'htp_app/detail_view.html'
    context_object_name = 'article'

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['category']).slug
        article = get_object_or_404(Article, slug=self.kwargs['article']).slug
        return Article.objects.filter(slug=article, category__slug=category)

    def get_context_data(self, **kwargs):
        request = self.request
        context = super().get_context_data(**kwargs)
        cookies = cookie_to_template(request)
        context.update(cookies)
        return context

    def get_object(self):
        return Article.objects.get(slug=self.kwargs.get('article'))


class InterviewListView(AllArticlesListView):
    queryset = Article.objects.all().filter(category__name='Собеседование')


class DocumentationListView(AllArticlesListView):
    queryset = Article.objects.all().filter(category__name='Документация')


class LibraryListView(AllArticlesListView):
    queryset = Article.objects.all().filter(category__name='Библиотеки')


class CheatsheetListView(AllArticlesListView):
    queryset = Article.objects.all().filter(category__name='Cheatsheets')


def documentation(request):
    context = {
        'test': 'doc page'
    }
    cookies = cookie_to_template(request)
    context.update(cookies)
    return render(request, 'htp_app/documentation.html', context)


def libraries(request):
    context = {
        'test': 'lib page'
    }
    cookies = cookie_to_template(request)
    context.update(cookies)
    return render(request, 'htp_app/libraries.html', context)


def cheatsheets(request):
    context = {
        'test': 'cheat page'
    }
    cookies = cookie_to_template(request)
    context.update(cookies)
    return render(request, 'htp_app/cheatsheets.html', context)


def interview(request):
    context = {
        'test': 'int page'
    }
    cookies = cookie_to_template(request)
    context.update(cookies)
    return render(request, 'htp_app/interview.html', context)


def forum(request):
    context = {
        'test': 'forum page'
    }
    cookies = cookie_to_template(request)
    context.update(cookies)
    return render(request, 'htp_app/forum.html', context)

