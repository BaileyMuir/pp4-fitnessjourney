from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import JournalPost
from .forms import JournalCommentForm

# Create your views here.

class JournalList(generic.ListView):
    model = JournalPost
    queryset = JournalPost.objects.filter(status=1).order_by('-created_on')
    template_name = 'journal.html'
    paginate_by = 4

class JournalDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = JournalPost.objects.filter(status=1)
        journalpost = get_object_or_404(queryset, slug=slug)
        journalcomments = journalpost.journalcomments.filter(message_approved=True).order_by('created_on')
        liked = False
        # if journalpost.journal_likes.filter(id=self.request.user.id).exhists():
        #     liked = True
        # disliked = False
        # if journalpost.journal_dislikes.filter(id=self.request.user.id).exhists():
        #     disliked = True

        return render(
            request,
             "journal_detail.html",
             {
                "journalpost": journalpost,
                "journalcomments": journalcomments,
                # "liked": liked,
                # "disliked": disliked,
                "Journal_Comment_Form": JournalCommentForm()
             },
        )