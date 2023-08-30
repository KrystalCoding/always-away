from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
from .models import Post, Comment, Photo
from .forms import CommentForm, PostForm, PhotoUploadForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.contenttypes.models import ContentType



class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):    
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        
        comment_ct = ContentType.objects.get_for_model(Post)
        comments = Comment.objects.filter(content_type=comment_ct, object_id=post.id, approved=True).order_by('-created_on')

        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            "post_detail.html",
            {
                "object": post,  # Use "object" instead of "post"
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
        comment_ct = ContentType.objects.get_for_model(Post)  # Define comment_ct here
        comments = Comment.objects.filter(content_type=comment_ct, object_id=post.id, approved=True).order_by('-created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.content_object = post
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
                "object": post,
                "comments": comments,
                "commented": commented,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    
@login_required
def edit_blog_comment(request, slug, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, approved=True)

    if comment.content_object.slug != slug:
        raise Http404("Comment does not belong to the specified post.")

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment updated successfully!")
            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'edit_blog_comment.html', {'form': form, 'comment': comment})



@login_required
def delete_blog_comment(request, slug, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, approved=True)

    if comment.content_object.slug != slug:
        raise Http404("Comment does not belong to the specified post.")

    if request.method == 'POST':
        comment.delete()
        messages.success(request, "Comment deleted successfully!")
        return redirect('post_detail', slug=slug)

    return render(request, 'delete_blog_comment.html', {'comment': comment})


@login_required
def edit_photo_comment(request, pk, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, approved=True)

    if comment.content_object.pk != pk:
        raise Http404("Comment does not belong to the specified post.")

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment updated successfully!")
            return redirect('photo_detail', pk=pk)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'edit_photo_comment.html', {'form': form, 'comment': comment})



@login_required
def delete_photo_comment(request, pk, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, approved=True)

    if comment.content_object.pk != pk:
        raise Http404("Comment does not belong to the specified post.")

    if request.method == 'POST':
        comment.delete()
        messages.success(request, "Comment deleted successfully!")
        return redirect('photo_detail', pk=pk)

    return render(request, 'delete_photo_comment.html', {'comment': comment})



class PostLike(View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

class PhotoLike(View):
    @staticmethod
    def post(request, pk):
        photo = get_object_or_404(Photo, pk=pk)

        if photo.likes.filter(id=request.user.id).exists():
            photo.likes.remove(request.user)
        else:
            photo.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('photo_detail', args=[pk]))


@login_required
def photo_like_view(request, pk):
    return PhotoLike.as_view()(request, pk=pk)


@login_required
def add_photo_comment(request, pk):
    photo = get_object_or_404(Photo, pk=pk)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.content_object = photo
            comment.name = request.user.username
            comment.approved = True
            comment.save()
            messages.success(request, "Comment posted successfully!")
            return redirect('gallery')

    comment_form = CommentForm()
    return render(request, 'add_photo_comment.html', {'photo': photo, 'comment_form': comment_form})


def photo_detail_view(request, pk):
    comment_ct = ContentType.objects.get_for_model(Photo)
    comments = Comment.objects.filter(content_type=comment_ct, object_id=pk, approved=True).order_by('-created_on')
    photo = get_object_or_404(Photo, pk=pk)
    ordered_comments = comments.order_by('-created_on')
    return render(request, 'photo_detail.html', {'photo': photo, 'comments': ordered_comments})


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
def edit_photo_view(request, pk):
    photo = get_object_or_404(Photo, pk=pk, uploaded_by=request.user)
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
def delete_photo_view(request, pk):
    photo = get_object_or_404(Photo, pk=pk, uploaded_by=request.user)
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
