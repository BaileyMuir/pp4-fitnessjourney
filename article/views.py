from django.shortcuts import render
from django.views import generic
from .models import Blog

class BlogList(generic.ListView):
    model = Blog
    queryset = Post.objects.filter(status=1).order_by('article_created_on')
    template_name = 'article.html'
    paginate_by = 6