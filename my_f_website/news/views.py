from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Categories


def index(request):
    news = News.objects.all()
    context = {'news': news,
               'title': 'Список новостей',
               }
    return render(request, 'news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Categories.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'category': category})
