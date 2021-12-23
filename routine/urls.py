from . import views
from django.urls import path


urlpatterns = [
    path("routine", views.WorkoutsList.as_view(), name='routine'),
    path('<slug:slug>/', views.WorkoutDetail.as_view(), name='workout_detail'),
]
