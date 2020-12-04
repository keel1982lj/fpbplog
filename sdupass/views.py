from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from userprofile.models import User
from django.contrib.auth.decorators import login_required
from article.models import ArticlePost
from django.http import HttpResponse

# Create your views here.

@login_required(login_url='/userprofile/login/')
def go_out(request):
    if request.user != User.objects.get(id=6):
        return HttpResponse("抱歉你没有权限")

    # 写死了，只支持我一个人用
    context = {"in_out": "批准出校"}
    return render(request, 'sdupass/pass.html', context=context)

@login_required(login_url='/userprofile/login/')
def go_in(request):
    if request.user != User.objects.get(id=6):
        return HttpResponse("抱歉你没有权限")

    # 写死了，只支持我一个人用
    context = {"in_out": "批准入校"}
    return render(request, 'sdupass/pass.html', context=context)