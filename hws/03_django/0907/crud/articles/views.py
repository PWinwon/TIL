from django.shortcuts import get_object_or_404, render, redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form,
        'chk': 'create', 
    }
    return render(request, 'articles/form.html', context)


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
        'chk': 'update',
    }
    return render(request, 'articles/form.html', context)


def delete(request, pk):
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', pk)