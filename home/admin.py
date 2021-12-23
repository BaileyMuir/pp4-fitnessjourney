from django.contrib import admin
from .models import MainPageContent
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(MainPageContent)
class HomeAdmin(SummernoteModelAdmin):
    summernote_fields = ('article_td', 'routines_td', 'recipies_td',)
