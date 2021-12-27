from django.shortcuts import render, HttpResponse
from django.views import generic

# Create your views here.

def HomeP(request):
    return render(request, 'index.html')
