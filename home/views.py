from django.shortcuts import render, HttpResponse
from django.views import generic

def HomeP(request):
    return render(request, 'index.html')
