from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('', include('articles/main')),
    # path('accounts/', include('accounts.urls')),
]
