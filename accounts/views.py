from django.shortcuts import render,redirect
from .forms import UserSignup
from django.contrib.messages import get_messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as my_login ,logout as my_logout 
from django.contrib.auth.decorators import login_required
from .models import NewUser

# Create your views here.



def signup(request):
    if request.method == 'POST':
        form = UserSignup(request.POST)
        if form.is_valid():
            form.save()
            my_login(request, form)
            return redirect('articles:main')
    else:
        form = UserSignup()
    context ={
        'signup_form' : form
    }
    return render(request,'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            my_login(request,form.get_user())
            return redirect(request.GET.get("next") or "articles:main")
    else:
        form = AuthenticationForm()
    context ={
        'login_form' : form
    }
    return render(request,'accounts/login.html',context)


def logout(request):
    my_logout(request)

    return redirect('articles:main')

@login_required
def detail(request):
    user_info = NewUser.objects.get(pk=request.user.pk)
    user_article = user_info.article_set.all()
    #참조 폴인키로 연결되어있는 오브젝트 반환
    print(user_article)
    context ={
        'user':user_info,
        'user_article':user_article
    }
    return render(request,'accounts/user_detail.html',context)
