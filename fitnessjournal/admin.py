from django.contrib import admin
from .models import JournalPost, JournalComment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(JournalPost)
class JournalAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'journal_content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('journal_content',)


@admin.register(JournalComment)
class JournalCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'message_body', 'journalpost', 'created_on', 'message_approved')
    list_filter = ('message_approved', 'created_on')
    search_fields = ('name', 'email', 'message_body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(message_approved=True)
