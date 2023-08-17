from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('create/', views.create_blog_post, name='create_blog_post'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
 