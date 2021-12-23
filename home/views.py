from django.shortcuts import render
from django.views import generic
from .models import MainPageContent

# Create your views here.


class MainPage(generic.ListView):
    model = MainPageContent
    template_name = 'index.html'
