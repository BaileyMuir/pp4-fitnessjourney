# Generated by Django 3.2 on 2021-12-22 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20211222_0119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='article_summery',
            new_name='article_exert',
        ),
    ]
