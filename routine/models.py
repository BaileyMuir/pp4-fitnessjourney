from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Posted"))

# had to make minor naming changes to fix errors to do with naming


class Workouts(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="workouts_posts")
    workouts_description = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    workouts_image = CloudinaryField('image', default='placeholder')
    workouts_created_on = models.DateTimeField(auto_now_add=True)
    exercise1 = models.CharField(max_length=100)
    tempo1 = models.CharField(max_length=100)
    reps1 = models.CharField(max_length=100)
    sets1 = models.CharField(max_length=100)
    rest1 = models.CharField(max_length=100)
    exercise2 = models.CharField(max_length=100)
    tempo2 = models.CharField(max_length=100)
    reps2 = models.CharField(max_length=100)
    sets2 = models.CharField(max_length=100)
    rest2 = models.CharField(max_length=100)
    exercise3 = models.CharField(max_length=100)
    tempo3 = models.CharField(max_length=100)
    reps3 = models.CharField(max_length=100)
    sets3 = models.CharField(max_length=100)
    rest3 = models.CharField(max_length=100)
    exercise4 = models.CharField(max_length=100)
    tempo4 = models.CharField(max_length=100)
    reps4 = models.CharField(max_length=100)
    sets4 = models.CharField(max_length=100)
    rest4 = models.CharField(max_length=100)
    exercise5 = models.CharField(max_length=100)
    tempo5 = models.CharField(max_length=100)
    reps5 = models.CharField(max_length=100)
    sets5 = models.CharField(max_length=100)
    rest5 = models.CharField(max_length=100)
    exercise6 = models.CharField(max_length=100)
    tempo6 = models.CharField(max_length=100)
    reps6 = models.CharField(max_length=100)
    sets6 = models.CharField(max_length=100)
    rest6 = models.CharField(max_length=100)
    exercise7 = models.CharField(max_length=100)
    tempo7 = models.CharField(max_length=100)
    reps7 = models.CharField(max_length=100)
    sets7 = models.CharField(max_length=100)
    rest7 = models.CharField(max_length=100)
    exercise8 = models.CharField(max_length=100)
    tempo8 = models.CharField(max_length=100)
    reps8 = models.CharField(max_length=100)
    sets8 = models.CharField(max_length=100)
    rest8 = models.CharField(max_length=100)
    status = models.IntegerField(choices=STATUS, default=0)
    workouts_likes = models.ManyToManyField(User, related_name='Workout_likes', blank=True)
    workouts_dislikes = models.ManyToManyField(User, related_name='Workout_dislikes', blank=True)

    class Meta:
        ordering = ['-workouts_created_on']

    def __str__(self):
        return self.title

    def article_total_likes(self):
        return self.workouts_likes.count()

    def article_total_dislikes(self):
        return self.workouts_dislikes.count()


class WorkoutsComment(models.Model):
    workout = models.ForeignKey(Workouts, on_delete=models.CASCADE, related_name='workoutscomments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.TimeField(auto_now_add=True)
    Workout_comment_approval = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"WorkoutsComment {self.name} {self.created_on} {self.message}"