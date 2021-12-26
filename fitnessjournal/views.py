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
        if journalpost.journal_likes.filter(id=self.request.user.id).exists():
            liked = True
        disliked = False
        if journalpost.journal_dislikes.filter(id=self.request.user.id).exists():
            disliked = True

        Journal_Comment_Form = JournalCommentForm(data=request.POST)

        if Journal_Comment_Form.is_valid():
            Journal_Comment_Form.instance.email = request.user.email
            Journal_Comment_Form.instance.name = request.user.username
            JournalComment = Journal_Comment_Form.save(commit=False)
            JournalComment.post = post
            JournalComment.save()
        else:
            Journal_Comment_Form = Journal_Comment_Form

        return render(
            request,
             "journal_detail.html",
             {
                "journalpost": journalpost,
                "journalcomments": journalcomments,
                "commented": False,
                "liked": liked,
                "disliked": disliked,
                "Journal_Comment_Form": JournalCommentForm()
             },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = JournalPost.objects.filter(status=1)
        journalpost = get_object_or_404(queryset, slug=slug)
        journalcomments = journalpost.journalcomments.filter(message_approved=True).order_by('created_on')
        liked = False
        if journalpost.journal_likes.filter(id=self.request.user.id).exists():
            liked = True
        disliked = False
        if journalpost.journal_dislikes.filter(id=self.request.user.id).exists():
            disliked = True

        Journal_Comment_Form = JournalCommentForm(data=request.POST)

        if Journal_Comment_Form.is_valid():
            Journal_Comment_Form.instance.email = request.user.email
            Journal_Comment_Form.instance.name = request.user.username
            JournalComment = Journal_Comment_Form.save(commit=False)
            JournalComment.post = post
            JournalComment.save()
        else:
            Journal_Comment_Form = Journal_Comment_Form

        return render(
            request,
             "journal_detail.html",
             {
                "journalpost": journalpost,
                "journalcomments": journalcomments,
                "commented": True,
                "liked": liked,
                "disliked": disliked,
                "Journal_Comment_Form": JournalCommentForm()
             },
        )