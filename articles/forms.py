from .models import Ariclee
from django import forms


class Article_form(forms.ModelForm):
    class Meta:
        model = Ariclee
        fields = ['title','context']
        labels = {
            "title" :"제목",
            "context":"상세내용",
        }