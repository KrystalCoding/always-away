import unittest

from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from blog.models import Post, Comment, Author, Category, Photo, Message

class BlogModelTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def create_test_post(self):
        return Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='This is a test content.'
        )

    def test_create_post(self):
        post = self.create_test_post()
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.slug, 'test-post')
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.content, 'This is a test content.')

    def test_create_comment(self):
        post = self.create_test_post()
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

    def test_comment_approval(self):
        post = self.create_test_post()
        comment = Comment.objects.create(
            content_type=ContentType.objects.get_for_model(Post),
            object_id=post.id,
            name='Test User',
            email='test@example.com',
            body='This is a test comment.',
            approved=False
        )
        self.assertFalse(comment.approved)

        comment.approved = True
        comment.save()

        updated_comment = Comment.objects.get(pk=comment.pk)
        self.assertTrue(updated_comment.approved)
