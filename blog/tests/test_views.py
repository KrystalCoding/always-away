import unittest

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from .models import Post, Comment, Author, Category, Photo, Message
from .views import YourViewClass


class BlogViewsTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))  # Adjust the URL name based on your actual URLs
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['post_list'], [])

    def test_post_detail_view(self):
        post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='This is a test content.'
        )
        response = self.client.get(reverse('post_detail', args=[post.slug]))  # Adjust the URL name based on your actual URLs
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['object'], post)
