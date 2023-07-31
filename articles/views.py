from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def main(request):
    all_articles= Article.objects.all()
    
    
    context = {
        "all_articles":all_articles 
    }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid:
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:main')
    else:
        print(request.user)
        form = ArticleForm()
    context= {
        'articleform' :form 
    }
    return render(request ,'articles/create.html',context)


def detail(request,pk):
    article = Article.objects.get(pk=pk)
    
    context = {
        "article":article,
    }
    return render(request,"articles/detail.html",context)

@login_required
def delete(request,pk):
    articles= Article.objects.get(pk=pk)
    if articles.user == request.user:
        articles.delete()
        return redirect('articles:main')