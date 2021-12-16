from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Posted"))


class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article_posts")
    updated_on = models.TimeField(auto_now=True)
    article_summery = models.TextField()
    article_image = CloudinaryField('image', default='placeholder')
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


class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='article_comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.TimeField(auto_now_add=True)
    blog_comment_approval = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Blog_comment {self.name} {self.created_on} {self.message}"
