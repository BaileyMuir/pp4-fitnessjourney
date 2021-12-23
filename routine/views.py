from django.shortcuts import render
from django.views import generic
from .models import Workout

# Create your views here.


class WorkoutsList(generic.ListView):
    model = Workout
    queryset = Workout.objects.filter(status=1).order_by('-workouts_created_on')
    template_name = 'routines.html'
    paginate_by = 6
