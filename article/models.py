from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


STATUS =((0, "Draft"), (1, "Posted"))


class Article(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article_posts")
    article_updated_on = models.TimeField(auto_now=True)
    article_summery = models.TextField()
    article_image = CloudinaryField('image', default='placeholder')
    article_video = CloudinaryField('video', default='placeholder')
    article_created_on = models.TimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    article_likes = models.ManyToManyField(User, related_name='article_likes', blank=True)
    article_dislikes = models.ManyToManyField(User, related_name='article_dislikes', blank=True)

    class Meta:
        ordering = ['-article_created_on']

    def __str__(self):
        return self.title

    def article_total_likes(self):
        return self.article_likes.count()

    def article_total_dislikes(self):
        return self.article_dislikes.count()

class Article_comments(models.Model):
    Article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    message_created_on = models.TimeField(auto_now_add=True)
    article_comment_approval = models.BooleanField(default=False)

    class Meta:
        ordering = ['-message_created_on']

    def __str__(self):
        return f"Article_comment {self.name} {self.message_created_on} {self.message} "
