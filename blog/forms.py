from .models import Comment
from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'featured_image', 'status']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
