"""
author:fp-bp
time:2020-11-23  21:54
"""

from django.db import models
# 内建的User模型
from django.contrib.auth.models import User
# timezone  用于处理时间相关事务
from django.utils import timezone
from django.urls import reverse

class ArticleColumn(models.Model):
    title = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

# 文章数据模型
class ArticlePost(models.Model):
    """
    使用ForeignKey定义一个关系，多个ArticlePost对象都关联到一个User对象。
    Django具有一个简单的账号系统，满足一般需求。
    每个字段都是Field类的实例。
    """
    # 文章作者，on_delete代表数据删除方式
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    # 更新时间，auto_now=True 指定每次更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)
    total_views = models.PositiveBigIntegerField(default=0)

    column = models.ForeignKey(ArticleColumn, null=True, blank=True, on_delete=models.CASCADE, related_name='article')

    # 内部类 class Meta 用于给model定义元数据
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列
        ordering = ('-created',)

    # 函数 __str__ 定义当调用对象的str() 方法时的返回值
    def __str__(self):
        # return self.title 将文章的标题返回
        return self.title

    def get_absolute_url(self):
        return reverse('article:article_detail', args=[self.id])