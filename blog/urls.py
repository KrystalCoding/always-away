from . import views
from django.urls import path

urlpatterns = [
    # Home page
    path('', views.PostList.as_view(), name='home'),
    
    # Message-related URLs
    path('send/', views.send_message, name='send_message'),
    path('edit/<int:message_id>/', views.edit_message, name='edit_message'),
    path('delete/<int:message_id>/', views.delete_message, name='delete_message'),
    path('save_as_draft/', views.save_as_draft, name='save_as_draft'),
    path('inbox/', views.inbox, name='inbox'),
    path('draft_inbox/', views.draft_inbox, name='draft_inbox'),
    path('message/<int:message_id>/', views.message_detail, name='message_detail'),
    path('delete_selected_messages/', views.delete_selected_messages, name='delete_selected_messages'),
    
    # Blog post-related URLs
    path('post/<slug:slug>/edit_comment/<int:comment_id>/', views.edit_blog_comment, name='edit_blog_comment'),
    path('post/<slug:slug>/delete_comment/<int:comment_id>/', views.delete_blog_comment, name='delete_blog_comment'),

    # Post interaction URLs
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
