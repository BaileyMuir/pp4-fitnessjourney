from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class MainPageContent(models.Model):
    home_image = CloudinaryField('image', default='placeholder')
    article_td = models.TextField()
    routines_td = models.TextField()
    recipies_td = models.TextField()
