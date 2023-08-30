from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    
    # path('create/', views.create_blog_post, name='create_blog_post'),
    
    path('gallery/', views.gallery_view, name='gallery'),
    path('upload_photo/', views.upload_photo_view, name='upload_photo'),
    path('photo/<pk>/', views.photo_detail_view, name='photo_detail'),
    path('edit_photo/<pk>/', views.edit_photo_view, name='edit_photo'),
    path('delete_photo/<pk>/', views.delete_photo_view, name='delete_photo'),
    path('like_photo/<pk>/', views.photo_like_view, name='photo_like'),
    path('add_photo_comment/<pk>/', views.add_photo_comment, name='add_photo_comment'),

    # For editing and deleting comments on photos
    path('photo/<pk>/edit_comment/<comment_id>/', views.edit_photo_comment, name='edit_photo_comment'),
    path('photo/<pk>/delete_comment/<comment_id>/', views.delete_photo_comment, name='delete_photo_comment'),
    
    # For editing and deleting comments on blog posts
    path('post/<slug:slug>/edit_comment/<int:comment_id>/', views.edit_blog_comment, name='edit_blog_comment'),
    path('post/<slug:slug>/delete_comment/<int:comment_id>/', views.delete_blog_comment, name='delete_blog_comment'),

    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]

 