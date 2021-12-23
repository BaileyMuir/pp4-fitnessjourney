from . import views
from django.urls import path


urlpatterns = [
    path("routine", views.WorkoutsList.as_view(), name='routine'),
]