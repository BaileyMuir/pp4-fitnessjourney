# Generated by Django 3.2 on 2021-12-22 01:12

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeroImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_image', cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/baileym/image/upload/v1638976391/sample.jpg', max_length=255, verbose_name='image')),
            ],
        ),
    ]
