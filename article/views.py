from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Blog
from .forms import ArticleCommentForm

class BlogList(generic.ListView):
    model = Blog
    queryset = Blog.objects.filter(status=1).order_by('-article_created_on')
    template_name = 'article.html'
    paginate_by = 6 
    paginate_by = 6

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Blog.objects.filter(status=1)
        blog = get_object_or_404(queryset, slug=slug)
        article_comments = blog.article_comments.filter(blog_comment_approval=True).order_by("-created_on")
        liked = False
        if blog.article_likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "blog": Blog,
                "article_comments": article_comments,
                "article_Commented": False,
                "liked": liked,
                "article_comment_form": ArticleCommentForm()
            },
        )