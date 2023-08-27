from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Post, Comment, Photo
from .forms import CommentForm, PostForm, PhotoUploadForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):    
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    @method_decorator(login_required)
    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = True
            comment.save()
            commented = True
            messages.success(request, "Comment posted successfully!")
        else:
            commented = False
            messages.error(request, "Failed to post comment. Please check your input.")
        
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )
    
@login_required
def edit_comment(request, slug, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, post__slug=slug, approved=True)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment updated successfully!")
            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'edit_comment.html', {'form': form, 'comment': comment})

@login_required
def delete_comment(request, slug, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, post__slug=slug, approved=True)
    if request.method == 'POST':
        comment.delete()
        messages.success(request, "Comment deleted successfully!")
        return redirect('post_detail', slug=slug)
    return render(request, 'delete_comment.html', {'comment': comment})

class PostLike(View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

@login_required
def gallery_view(request):
    photos = Photo.objects.all()
    context = {'photos': photos}
    return render(request, 'gallery.html', context)

@login_required
def upload_photo_view(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            new_photo = form.save(commit=False)
            new_photo.uploaded_by = request.user
            new_photo.save()
            messages.success(request, "Photo uploaded successfully!")
            return redirect('gallery')
    else:
        form = PhotoUploadForm()
    context = {'form': form}
    return render(request, 'upload_photo.html', context)

@login_required
def edit_photo_view(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id, uploaded_by=request.user)
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            messages.success(request, "Photo updated successfully!")
            return redirect('gallery')
    else:
        form = PhotoUploadForm(instance=photo)
    context = {'form': form, 'photo': photo}
    return render(request, 'edit_photo.html', context)

@login_required
def delete_photo_view(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id, uploaded_by=request.user)
    if request.method == 'POST':
        photo.delete()
        messages.success(request, "Photo deleted successfully!")
        return redirect('gallery')
    context = {'photo': photo}
    return render(request, 'delete_photo.html', context)



#@login_required
#def create_blog_post(request):
#   if request.method == 'POST':
#       form = PostForm(request.POST)
#       if form.is_valid():
#           new_post = form.save(commit=False)
#           new_post.author = request.user
#           new_post.save()
#           messages.success(request, 'Your post has been created!')
#           return redirect('blog:index')
#   else:
#       form = PostForm()
#   return render(request, 'blog/create_post.html', {'form': form})
