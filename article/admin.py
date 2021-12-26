from django.contrib import admin
from .models import Blog, BlogComment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Blog)
class BlogAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'article_created_on')
    search_fields = ['title', 'article_content']
    list_filter = ('status', 'article_created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('article_content',)

@admin.register(BlogComment)
class BCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'blog', 'created_on', 'blog_comment_approval')
    list_filter = ('blog_comment_approval', 'created_on')
    search_fields = ('name', 'email', 'message')
    actions = ['blog_approve_comments']
    
    def blog_approve_comments(self, request, queryset):
        queryset.update(blog_comment_approval=True)
