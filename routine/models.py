from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Posted"))

# had to make minor naming changes to fix errors to do with naming


class Workout(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workouts_posts")
    workouts_description = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    workouts_image = CloudinaryField('image', default='placeholder')
    workouts_created_on = models.DateTimeField(auto_now_add=True)
    workouts_content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    workouts_likes = models.ManyToManyField(User, related_name='Workout_likes', blank=True)
    workouts_dislikes = models.ManyToManyField(User, related_name='Workout_dislikes', blank=True)

    class Meta:
        ordering = ['-workouts_created_on']

    def __str__(self):
        return self.title

    def workout_total_likes(self):
        return self.workouts_likes.count()

    def workout_total_dislikes(self):
        return self.workouts_dislikes.count()


class WorkoutsComment(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='workoutscomments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.TimeField(auto_now_add=True)
    Workout_comment_approval = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"WorkoutsComment {self.name} {self.created_on} {self.message}"
