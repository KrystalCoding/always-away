from .models import Comment, Post, Photo, Message
from django import forms
from . import models


class PostForm(forms.ModelForm):
    title = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Title"
        })
    )    
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a Post!"
        })
    )
    class Meta:
       model = Post
       fields = ['title', 'content', 'featured_image', 'status']

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Get the user from kwargs
        super().__init__(*args, **kwargs)
        if user:
            self.fields['author'].initial = user.username


class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('image', 'caption')
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({'class': 'form-control-file'})
        self.fields['caption'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Caption'})

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['subject', 'content']
