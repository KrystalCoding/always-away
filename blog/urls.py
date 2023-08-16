from . import views
from django.urls import path


# app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('create/', views.create_blog_post, name='create_blog_post'),
]
 