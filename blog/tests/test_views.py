from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from blog.models import Post, Comment, Message
from blog.views import PostList, PostDetail, PostLike, inbox, draft_inbox, message_detail, send_message, save_as_draft, edit_message, delete_message, delete_selected_messages


class BlogViewsTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_view(self):
        # Create a test post with the test user as the author
        post = Post.objects.create(
            title='Test Post',
            content='This is a test content.',
            status=1, # Assuming 1 is the published status
            author=self.user
        )

        # Print the generated URL for debugging
        print("Generated URL:", reverse('post_detail', kwargs={'slug': post.slug}))

        response = self.client.get(reverse('post_detail', kwargs={'slug': post.slug}))

        # Print the content of the response for debugging
        print(response.content.decode('utf-8')) # Add this line
        self.assertEqual(response.status_code, 200)


    def test_edit_blog_comment_view(self):
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
        self.assertEqual(response.status_code, 302)

    def test_delete_blog_comment_view(self):
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
        self.assertEqual(response.status_code, 302)

    def test_post_like_view(self):
        self.client.login(username='testuser', password='testpassword')  # Authenticate the user
        post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='This is a test content.'
        )
        response = self.client.post(reverse('post_like', args=[post.slug]))
        self.assertEqual(response.status_code, 302)  # Assuming a redirect upon successful like

