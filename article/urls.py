from . import views
from django.urls import path


urlpatterns = [
    path("article", views.BlogList.as_view(), name='article'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
] 