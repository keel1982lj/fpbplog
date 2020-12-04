from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import ArticlePost, ArticleColumn
from .forms import ArticlePostForm
import markdown
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from comment.models import Comment


def article_list(request):
    search = request.GET.get('search')
    order = request.GET.get('order')

    if search:
        if order == 'total_views':
            article_list = ArticlePost.objects.filter(
                Q(title__icontains=search)|
                Q(body__icontains=search)
            ).order_by('-total_views')
        else:
            article_list = ArticlePost.objects.filter(
                Q(title__icontains=search) |
                Q(body__icontains=search)
            )
    else:
        search = ''
        if order == 'total_views':
            article_list = ArticlePost.objects.all().order_by('-total_views')
        else:
            article_list = ArticlePost.objects.all()

    paginator = Paginator(article_list, 2)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    # show_status 代表显示类型  1是卡片式  2是列表式
    context = {'articles': articles, 'order': order, 'search': search, 'show_status': 2}
    return render(request, 'article/list.html', context)


def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra', 'markdown.extensions.codehilite', 'markdown.extensions.toc',
        'markdown.extensions.tables'
    ])
    article.body = md.convert(article.body)
    article.total_views += 1
    article.save(update_fields=['total_views'])

    comments = Comment.objects.filter(article=id)
    context = {"article": article, 'toc': md.toc, 'comments': comments}
    return render(request, 'article/detail.html', context)

@login_required(login_url='/userprofile/login/')
def article_create(request):
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            new_article = article_post_form.save(commit=False)
            new_article.author = User.objects.get(id=request.user.id)
            new_article.save()
            return redirect("article:article_list")
        else:
            return HttpResponse("表单内容有误，请从新填写。")
    else:
        article_post_form = ArticlePostForm()
        columns = ArticleColumn.objects.all()
        context = {"article_post_form": article_post_form, "columns": columns}
        return render(request, 'article/create.html', context)

@login_required(login_url='/userprofile/login/')
def article_delete(request, id):
    if request.method == 'POST':
        article = ArticlePost.objects.get(id=id)
        if article.author != request.user:
            return HttpResponse("抱歉，你没有权限修改文章")
        article.delete()
        return redirect("article:article_list")
    else:
        return HttpResponse("仅允许post请求")

@login_required(login_url='/userprofile/login/')
def article_update(request, id):
    article = ArticlePost.objects.get(id=id)
    columns = ArticleColumn.objects.all()
    if article.author != request.user:
        return HttpResponse("抱歉，你没有权限修改文章")
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.column = columns.get(id=request.POST['column'])
            article.save()
            return redirect("article:article_detail", id=id)
        else:
            return HttpResponse("表单有误，请重新填写")
    else:
        article_post_form = ArticlePostForm()
        context = {'article': article, 'article_post_form': article_post_form, "columns": columns}
        return render(request, 'article/update.html', context)
