from . import views
from django.urls import path


urlpatterns = [
    path("article", views.BlogList.as_view(), name='article')
]