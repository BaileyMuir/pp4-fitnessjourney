from . import views
from django.urls import path


urlpatterns = [
    path("home", views.MainPage.as_view(), name='home')
]