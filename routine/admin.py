from django.contrib import admin
from .models import Workouts, WorkoutsComment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Workouts)
class WorkoutsAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'workouts_created_on')
    search_fields = ['title', 'workouts_description']
    list_filter = ('status', 'workouts_created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('exercise1', 'tempo1', 'reps1',
     'sets1', 'rest1', 'exercise2', 'tempo2', 'reps2',
     'sets2', 'rest2', 'exercise3', 'tempo3', 'reps3',
     'sets3', 'rest3', 'exercise4', 'tempo4', 'reps4',
     'sets4', 'rest4', 'exercise5', 'tempo5', 'reps5',
     'sets5', 'rest5', 'exercise6', 'tempo6', 'reps6',
     'sets6', 'rest6', 'exercise7', 'tempo7', 'reps7',
     'sets7', 'rest7', 'exercise8', 'tempo8', 'reps8',
     'sets8', 'rest8',)


@admin.register(WorkoutsComment)
class WCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'workout', 'created_on', 'Workout_comment_approval')
    list_filter = ('Workout_comment_approval', 'created_on')
    search_fields = ('name', 'email', 'message')
    actions = ['workout_approve_comments']

    def workout_approve_comments(self, request, queryset):
        queryset.update(Workout_comment_approval=True)
