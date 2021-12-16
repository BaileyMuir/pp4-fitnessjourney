from django.contrib import admin
from .models import Blog
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Blog)
class BlogAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'article_created_on')
    search_fields = ['title', 'article_summery']
    list_filter = ('status', 'article_created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('article_summery',)