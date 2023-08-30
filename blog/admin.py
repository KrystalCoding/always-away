from django.contrib import admin
from .models import Post, Comment, Photo, Author#, Category
from django.contrib.contenttypes.admin import GenericTabularInline
from django_summernote.admin import SummernoteModelAdmin


class CommentInline(GenericTabularInline):
    model = Comment
    extra = 0


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content',)

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = ('image', 'caption', 'uploaded_by', 'uploaded_on')
    search_fields = ('caption', 'uploaded_by__username', 'uploaded_on')
    list_filter = ('uploaded_on',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = ('User', 'profile_picture')
    search_fields = ('User__username',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'content_object_display', 'created_on', 'approved')
    list_filter = ('approved', 'created_on', 'content_type')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

    def content_object_display(self, obj):
        if hasattr(obj.content_object, 'title'):
            return obj.content_object.title
        elif hasattr(obj.content_object, 'caption'):
            return obj.content_object.caption
        else:
            return None

    content_object_display.short_description = 'Content Object'

class PostWithCommentsAdmin(PostAdmin):
    inlines = [CommentInline]

class PhotoWithCommentsAdmin(PhotoAdmin):
    inlines = [CommentInline]

admin.site.unregister(Post)
admin.site.unregister(Photo)
admin.site.unregister(Author)
admin.site.unregister(Comment)

admin.site.register(Post, PostWithCommentsAdmin)
admin.site.register(Photo, PhotoWithCommentsAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment, CommentAdmin)
