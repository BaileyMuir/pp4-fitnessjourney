from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Posted"))

# had to make minor naming changes to fix errors to do with naming


class Posts(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs_posts")
    post_description = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    post_image = CloudinaryField('image', default='placeholder')
    post_created_on = models.DateTimeField(auto_now_add=True)
    post_content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    post_likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    post_dislikes = models.ManyToManyField(User, related_name='post_dislikes', blank=True)

    class Meta:
        ordering = ['-post_created_on']

    def __str__(self):
        return self.title

    def post_total_likes(self):
        return self.post_likes.count()

    def post_total_dislikes(self):
        return self.post_dislikes.count()


class PostsComment(models.Model):
    Posts = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='postscomments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.TimeField(auto_now_add=True)
    post_comment_approval = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"postComment {self.name} {self.created_on} {self.message}"
