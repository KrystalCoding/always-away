import unittest

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from .models import Post, Comment


class BlogURLTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_post_list_url(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url(self):
        post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='This is a test content.'
        )
        response = self.client.get(reverse('post_detail', args=[post.slug]))
        self.assertEqual(response.status_code, 200)

    def test_edit_blog_comment_url(self):
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
            body='This is a test comment.',
            approved=True
        )
        response = self.client.get(reverse('edit_blog_comment', args=[post.slug, comment.id]))
        self.assertEqual(response.status_code, 200)

    def test_delete_blog_comment_url(self):
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
            body='This is a test comment.',
            approved=True
        )
        response = self.client.get(reverse('delete_blog_comment', args=[post.slug, comment.id]))
        self.assertEqual(response.status_code, 200)

    # Add more URL tests as needed for other views
