from django.shortcuts import render, redirect, get_object_or_404

from .models import Article
from .forms import ArticleForm
from django.contrib import messages
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



def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.user == article.user: 
        if request.method == 'POST':
            # POST : input 값 가져와서, 검증하고, DB에 저장
            article_form = ArticleForm(request.POST, request.FILES, instance=article)
            if article_form.is_valid():
                # 유효성 검사 통과하면 저장하고, 상세보기 페이지로
                article_form.save()
                messages.success(request, '글이 수정되었습니다.')
                return redirect('articles:detail', article.pk)
            # 유효성 검사 통과하지 않으면 => context 부터해서 오류메시지 담긴 article_form을 랜더링
        else:
            # GET : Form을 제공
            article_form = ArticleForm(instance=article)
        context = {
            'article_form': article_form
        }
        return render(request, 'articles/form.html', context)
    else:
        # 작성자가 아닐 때
        # (1) 403 에러메시지를 던져버린다. 
        # from django.http import HttpResponseForbidden
        # return HttpResponseForbidden()
        # (2) flash message 활용!
        messages.warning(request, '작성자만 수정할 수 있습니다.')
        return redirect('articles:detail', article.pk)