from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import JournalPost
from .forms import JournalCommentForm


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

        return render(
            request,
            "journal_detail.html",
            {
                "journalpost": journalpost,
                "journalcomments": journalcomments,
                "commented": False,
                "liked": liked,
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

        journal_comment_form = JournalCommentForm(data=request.POST)
        if journal_comment_form.is_valid():
            journal_comment_form.instance.email = request.user.email
            journal_comment_form.instance.name = request.user.username
            journalcomment = journal_comment_form.save(commit=False)
            journalcomment.journalpost = journalpost
            journalcomment.save()
        else:
            journal_comment_form = JournalCommentForm()

        return render(
            request,
            "journal_detail.html",
            {
                "journalpost": journalpost,
                "journalcomments": journalcomments,
                "commented": True,
                "journal_comment_form": journal_comment_form,
                "liked": liked,
            },
        )
