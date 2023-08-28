from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
# path('create/', views.create_blog_post, name='create_blog_post'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('upload_photo/', views.upload_photo_view, name='upload_photo'),
    path('edit_photo/<int:photo_id>/', views.edit_photo_view, name='edit_photo'),
    path('delete_photo/<int:photo_id>/', views.delete_photo_view, name='delete_photo'),
    path('like_photo/<int:photo_id>/', views.photo_like_view, name='photo_like'),
    path('add_photo_comment/<int:photo_id>/', views.add_photo_comment, name='add_photo_comment'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('<slug:slug>/delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]

 