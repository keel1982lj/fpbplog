from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from .models import Comment
from userprofile.models import User
from django.contrib.auth.decorators import login_required
from article.models import ArticlePost
from django.http import HttpResponse

@login_required(login_url='/userprofile/login/')
def post_comment(request, article_id):
    article = get_object_or_404(ArticlePost, id=article_id)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.article = article
            new_comment.user = request.user
            new_comment.save()
            return redirect(article)
        else:
            return HttpResponse("表单内容有误,请重新填写")
    else:
        return HttpResponse("只接受post请求")

@login_required(login_url='/userprofile/login/')
def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    article = get_object_or_404(ArticlePost, id=comment.article_id)
    if request.user != comment.user:
        return HttpResponse("没有权限！")
    else:
        comment.delete()
        return redirect(article)

