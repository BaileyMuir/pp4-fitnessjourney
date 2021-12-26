from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class JournalPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="journal_posts"
    )
    journal_featured_image = CloudinaryField('image', default='placeholder')
    journal_excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    journal_content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    journal_likes = models.ManyToManyField(
        User, related_name='journal_like', blank=True)
    journal_dislikes = models.ManyToManyField(
        User, related_name='journal_dislike', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.journal_likes.count()

    def number_of_dislikes(self):
        return self.journal_dislikes.count()


class JournalComment(models.Model):
    journalpost = models.ForeignKey(JournalPost, on_delete=models.CASCADE,
                             related_name="journalcomments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    message_body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    message_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"JournalComment {self.message_body} by {self.name}"