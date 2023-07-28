from django.shortcuts import render,redirect
from .models import Article
from .forms import Article_form

# Create your views here.

def main(request):
    all_articles= Article.objects.all()
    
    
    context = {
        all_articles:"all_articles"
    }
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        form = Article_form(request.POST)
        if form.is_valid:
            form.save()
            return redirect('articles:main')
    else:
        form = Article_form()
    context= {
        form : 'form'
    }
    return render(request ,'articles/create.html',context)


# def create(request):
#     if request.method == "POST":
#         request.context = 