from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

#class Category(models.Model):
#    name = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    local_featured_image = models.ImageField(upload_to='images/', blank=True, null=True)
    cloudinary_featured_image = models.URLField(blank=True, null=True)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blogpost_like', blank=True)
#   categories = models.ManyToManyField('Category', related_name='posts')

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True,)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

class Author(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Photo(models.Model):
    image = models.ImageField(upload_to='images/')
    cloudinary_image = CloudinaryField("image")
    caption = models.CharField(max_length=200, blank=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    uploaded_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='photo_likes', blank=True)

    def __str__(self):
        return self.caption or 'Photo'

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    recipient = models.ManyToManyField(User, related_name='received_messages')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    is_draft = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
