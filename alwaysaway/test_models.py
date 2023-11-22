import unittest

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from .models import Post, Comment

class BlogModelTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_post(self):
        post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='This is a test content.'
        )
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.slug, 'test-post')
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.content, 'This is a test content.')

    def test_create_comment(self):
        post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='This is a test content.'
        )
        comment = Comment.objects.create(
            content_type=ContentType.objects.get_for_model(Post),
            object_id=post.id,
            name='Test User',
            email='test@example.com',
            body='This is a test comment.'
        )
        self.assertEqual(comment.name, 'Test User')
        self.assertEqual(comment.email, 'test@example.com')
        self.assertEqual(comment.body, 'This is a test comment.')

