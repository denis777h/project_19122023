from urllib import response, request

from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.template.defaultfilters import censor
from .models import NewsArticle
import request





class NewsListView(ListView):
    model = NewsArticle
    template_name = 'default.html'
    context_object_name = 'default'
    ordering = ['-publication_date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['censor'] = censor
        return context


    def news_list(request):
        news_list = NewsArticle.objects.all()
        paginator = Paginator(news_list, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    pass

    def news_search(request):
        query = request.GET.get('query')
        news_list = News.objects.filter(title__icontains=query) | News.objects.filter(
            author__icontains=query) | NewsArticle.objects.filter(date__gt=query)
        paginator = Paginator(news_list, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, '', {'page_obj': page_obj, 'query': query})


class NewsDetailView(DetailView):
    model = NewsArticle
    template_name = 'default.html'
    context_object_name = 'news_article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['censor'] = censor
        return context


class NewsCreateView(CreateView):
    model = NewsArticle
    template_name = 'default.html'
    context_object_name = 'news_article'


class NewsUpdateView(UpdateView):
    model = NewsArticle
    model = NewsArticle
    template_name = 'default.html'
    context_object_name = 'news_article'


class NewsDelete(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')



