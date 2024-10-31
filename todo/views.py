from django.shortcuts import render, get_object_or_404
from .models import Article

def home(request):
    articles = Article.objects.all()
    return render(request, 'home.html', {'articles': articles})

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'detail.html', {'article': article})
