from django.shortcuts import render
from django.views import generic
from .models import HeroImage

# Create your views here.
class MainPage(generic.ListView):
    model = HeroImage
    template_name = 'index.html'