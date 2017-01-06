from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.tag_name

class Article(models.Model):
    title = models.CharField(max_length = 256)  # blog 题目
    category = models.CharField(max_length = 50, blank = True) # blog 标签
    date_time = models.DateTimeField(auto_now_add = True) # blog 日期
    content = models.TextField(blank = True, null = True) # blog 文章正文

    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id':self.id})
        return "http://127.0.0.1:8000%s" % path

    def __str__(self):
        return self.title

    class Meta: # 按时间顺序排序
        ordering = ['-date_time']