from django.contrib import admin
from .models import Post, Comment, Photo, Author#, Category
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'content_type', 'object_title', 'created_on', 'approved')
    list_filter = ('approved', 'created_on', 'content_type')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
    
    def object_title(self, obj):
        return obj.content_object.title

    def content_type(self, obj):
        return obj.content_type.name

    object_title.short_description = 'Object Title'
    content_type.short_description = 'Content Type'

admin.site.register(Photo)
