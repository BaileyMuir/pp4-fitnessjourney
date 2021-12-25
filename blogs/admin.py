from django.contrib import admin
from .models import Posts, PostsComment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Posts)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'post_created_on')
    search_fields = ['title', 'post_description']
    list_filter = ('status', 'post_created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('post_content',)


@admin.register(PostsComment)
class PCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'Posts', 'created_on', 'post_comment_approval')
    list_filter = ('post_comment_approval', 'created_on')
    search_fields = ('name', 'email', 'message')
    actions = ['post_approve_comments']

    def workout_approve_comments(self, request, queryset):
        queryset.update(Workout_comment_approval=True)
