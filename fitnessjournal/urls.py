from .import views
from django.urls import path

urlpatterns = [
    path('journals', views.JournalList.as_view(), name='journals')
]