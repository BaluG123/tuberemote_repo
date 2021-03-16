from django.contrib import admin
from testapp.models import Video,Comment,Profile

class VideoAdmin(admin.ModelAdmin):
    list_display=['id','video','image','title','user','publish','uploaded','updated','status']
    list_filter=('uploaded',)
    date_hierarchy='uploaded'
    prepopulated_fields={'slug':('title',)}
    search_fields=('title','tags','video')
    raw_id_fields=('user',)

class CommentAdmin(admin.ModelAdmin):
    list_display=['video','comment','user','commented','updated','active']
    list_filter=('commented','user')
    search_fields=('comment','user')
    date_hierarchy='commented'

class ProfileAdmin(admin.ModelAdmin):
    list_display=['firstname','email','profilepic','birthday','bio','gender','created','updated']
    prepopulated_fields={'firstname':('username',)}
    search_fields=('firstname',)
    date_hierarchy='created'


# Register your models here.
admin.site.register(Video,VideoAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Profile,ProfileAdmin)
