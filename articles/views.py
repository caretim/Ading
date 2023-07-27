from django.shortcuts import render,redirect
from .models import Article
# Create your views here.

def main(request):
    
    
    return render(request, 'articles/index.html')

# def create(request):
#     if request.method == "POST":
#         request.context = 