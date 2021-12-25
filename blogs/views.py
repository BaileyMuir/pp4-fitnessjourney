from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Workout

# Create your views here.


class Postslists(generic.ListView):
    model = Posts
    queryset = posts.objects.filter(status=1).order_by('-post_created_on')
    template_name = 'routines.html'
    paginate_by = 6

class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Posts.objects.filter(status=1)
        posts = get_object_or_404(queryset, slug=slug)
        postscomment = posts.postcomment.filter(posts_comment_approval=True).order_by("-created_on")
        liked = False
        if posts.workouts_likes.filter(id=self.request.user.id).exists():
            liked = True
            
        return render(
            request,
            "blogs_detail.html",
            {
                "posts": posts,
                "postcomments": workoutscomments,
                "liked": liked
            },
        )
