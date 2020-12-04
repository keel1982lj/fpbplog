from django import forms
from .models import ArticlePost

# 文章的表单类
class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ('title', 'body', 'column')