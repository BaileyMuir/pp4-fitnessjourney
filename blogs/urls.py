from . import views
from django.urls import path


urlpatterns = [
    path("blogs", views.Postslists.as_view(), name='blogs'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]