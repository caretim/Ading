from .models import Article
from django import forms


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content']
        # labels = {
        #     "title" :"제목",
        #     "content":"상세내용",
        # }


