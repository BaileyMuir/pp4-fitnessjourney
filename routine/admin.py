from django.contrib import admin
from .models import Workout, WorkoutsComment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Workout)
class WorkoutAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'workouts_created_on')
    search_fields = ['title', 'workouts_description']
    list_filter = ('status', 'workouts_created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('workouts_content',)


@admin.register(WorkoutsComment)
class WCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'workout', 'created_on', 'Workout_comment_approval')
    list_filter = ('Workout_comment_approval', 'created_on')
    search_fields = ('name', 'email', 'message')
    actions = ['workout_approve_comments']

    def workout_approve_comments(self, request, queryset):
        queryset.update(Workout_comment_approval=True)
