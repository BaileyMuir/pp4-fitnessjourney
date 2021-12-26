from django.shortcuts import render
from django.views import generic
from .models import JournalPost

# Create your views here.

class JournalList(generic.ListView):
    model = JournalPost
    queryset = JournalPost.objects.filter(status=1).order_by('-created_on')
    template_name = 'journal.html'
    paginate_by = 4