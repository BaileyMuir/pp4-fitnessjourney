from .import views
from django.urls import path

urlpatterns = [
    path('journals', views.JournalList.as_view(), name='journals'),
    path('<slug:slug>/', views.JournalDetail.as_view(), name='journal_detail'),
]
