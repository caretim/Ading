from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'articles'

urlpatterns = [
    path('',views.main,name='main'),
    path('create/' ,views.create, name='create'),
    path("detail/<int:pk>/",views.detail,name = "detail"),
    path("delete/<int:pk>/",views.delete,name = "delete"),
    # path('accounts/', include('accounts.urls')),
]
