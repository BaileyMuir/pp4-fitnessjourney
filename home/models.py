from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class HeroImage(models.Model):
    home_image = CloudinaryField('image', default='https://res.cloudinary.com/baileym/image/upload/v1638976391/sample.jpg')