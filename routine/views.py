from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Workout

# Create your views here.


class WorkoutsList(generic.ListView):
    model = Workout
    queryset = Workout.objects.filter(status=1).order_by('-workouts_created_on')
    template_name = 'routines.html'
    paginate_by = 6

class WorkoutDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Workout.objects.filter(status=1)
        workout = get_object_or_404(queryset, slug=slug)
        workoutscomments = workout.workoutscomments.filter(Workout_comment_approval=True).order_by("-created_on")
        liked = False
        if workout.workouts_likes.filter(id=self.request.user.id).exists():
            liked = True
            
        return render(
            request,
            "routine_detail.html",
            {
                "workout": workout,
                "workoutscomments": workoutscomments,
                "liked": liked
            },
        )

