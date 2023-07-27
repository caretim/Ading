from django.shortcuts import render,redirect
from .forms import UserSignup
# Create your views here.



def signup(request):
    if request.method == 'POST':
        form = UserSignup(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:main')
    else:
        form = UserSignup()
        context ={
            'signup_form' : form
        }
    return render(request,'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        form = UserSignup(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articlse:main')
    else:
        form = UserSignup()
        context ={
            'signup_form' : form
        }
    return render(request,'accounts/signup.html',context)
