from django.shortcuts import render,redirect

from .models import Article
from .forms import ArticleForm
# Create your views here.



def index(request):
    articles=Article.objects.order_by('pk')
    context ={
        'articles':articles
    }
    return render (request,'articles/index.html',context)


def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid(): #유효성검사
            article = article_form.save(commit=True)# 유효하다면 데이터베이스 커밋,
            article.save()
            return redirect('articles:index') # 글 작성후 바로 인덱스페이지로 이동하기,
    else: # 메소드가 post가 아닐시, 빈 폼을 줘서 작성양식을 보여준다,
        article_form = ArticleForm()
        context = {
            'article_form':article_form
        }
        return render(request,'articles:form.html', context=context)
    