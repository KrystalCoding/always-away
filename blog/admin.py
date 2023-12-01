from django.contrib import admin
from .models import Post, Comment, Photo, Author, Message
from django.contrib.auth.models import User
from django.contrib.contenttypes.admin import GenericTabularInline
from django_summernote.admin import SummernoteModelAdmin


class CommentInline(GenericTabularInline):
    """
    Inline for displaying comments in the admin panel.
    """

    model = Comment
    extra = 0


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the Post model.
    """

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content',)
    fields = ('title', 'slug', 'author', 'content', 'local_featured_image', 'cloudinary_featured_image', 'excerpt', 'status', 'likes')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Photo model.
    """

    list_display = ('image', 'caption', 'uploaded_by', 'uploaded_on')
    search_fields = ('caption', 'uploaded_by__username', 'uploaded_on')
    list_filter = ('uploaded_on',)
    fields = ('image', 'caption', 'uploaded_by')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Author model.
    """

    list_display = ('User', 'profile_picture')
    search_fields = ('User__username',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Comment model.
    """

    list_display = ('name', 'body', 'content_object_display', 'created_on', 'approved')
    list_filter = ('approved', 'created_on', 'content_type')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        Action to approve selected comments.
        """

        queryset.update(approved=True)

    def content_object_display(self, obj):
        """
        Display the related content object in the admin panel.
        """

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


admin.site.register(Message)

def send_message_to_users(modeladmin, request, queryset):
    """
    Action to send a message to selected users.
    """
    
    for user in queryset:
        message = Message.objects.create(
            sender=request.user,
            subject="Your Subject Here",
            content="Your Content Here",
            is_draft=False,
        )
        message.recipient.add(user)

send_message_to_users.short_description = "Send message to selected users"

class UserAdmin(admin.ModelAdmin):
    actions = [send_message_to_users]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)