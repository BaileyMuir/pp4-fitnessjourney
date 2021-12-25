from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Posts

# Create your views here.


class Postslists(generic.ListView):
    model = Posts
    queryset = Posts.objects.filter(status=1).order_by('-post_created_on')
    template_name = 'blogs.html'
    paginate_by = 6

class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Posts.objects.filter(status=1)
        posts = get_object_or_404(queryset, slug=slug)
        postscomments = posts.postscomments.filter(post_comment_approval=True).order_by("-created_on")
        liked = False
        if posts.post_likes.filter(id=self.request.user.id).exists():
            liked = True
            
        return render(
            request,
            "blogs_detail.html",
            {
                "posts": posts,
                "postcomments": postscomments,
                "commented": False,
                "liked": liked
            },
        )
