from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect, Http404
from django.contrib import messages
from .models import Post, Comment, Photo, Message
from .forms import CommentForm, PostForm, PhotoUploadForm, MessageForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import DetailView



class PostList(generic.ListView):
    """View to display a paginated list of posts."""

    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(DetailView):
    """View to display details of a single post and associated comments."""


    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'object'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        """Add additional context data for post detail view."""

        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(
            content_type=ContentType.objects.get_for_model(Post),
            object_id=self.object.id,
            approved=True
        ).order_by('-created_on')

        context['liked'] = self.object.likes.filter(id=self.request.user.id).exists()
        context['comment_form'] = CommentForm()

        return context


    @method_decorator(login_required)
    def post(self, request, slug, *args, **kwargs):
        """Handle POST requests for adding comments to a post."""
        
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
    """View to edit a blog comment."""
    
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
    """View to delete a blog comment."""
    
    comment = get_object_or_404(Comment, id=comment_id, approved=True)

    if comment.content_object.slug != slug:
        raise Http404("Comment does not belong to the specified post.")

    if request.method == 'POST':
        comment.delete()
        messages.success(request, "Comment deleted successfully!")
        return redirect('post_detail', slug=slug)

    return render(request, 'delete_blog_comment.html', {'comment': comment})



class PostLike(View):
    """View to handle liking/unliking a post."""

    def post(self, request, slug):
        """Handle POST requests for liking/unliking a post."""

        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))



@login_required
def inbox(request):
    """View to display the inbox of a user."""

    messages = Message.objects.filter(sender=request.user, is_draft=False).order_by('-created_at')
    return render(request, 'inbox.html', {'messages': messages})

@login_required
def draft_inbox(request):
    """View to display the draft messages of a user."""

    draft_messages = Message.objects.filter(sender=request.user, is_draft=True).order_by('-created_at')
    return render(request, 'draft_inbox.html', {'draft_messages': draft_messages})

@login_required
def message_detail(request, message_id):
    """View to display the details of a single message."""

    message = get_object_or_404(Message, id=message_id, sender=request.user)
    return render(request, 'message_detail.html', {'message': message})

@login_required
def send_message(request):
    """View to handle sending a message."""

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.is_draft = 'save_as_draft' in request.POST
            admin_user = get_object_or_404(User, username='admin')
            message.save()

            message.recipient.set([admin_user])

            if not message.is_draft:
                message.recipient.set([admin_user])
                message.save()
                return redirect('inbox')

            if message.is_draft:
                return redirect('draft_inbox')
            else:
                return redirect('inbox')
    else:
        form = MessageForm()
    return render(request, 'send_message.html', {'form': form})



@login_required
def save_as_draft(request):
    """View to save a message as a draft."""

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.is_draft = True
            message.save()
            return redirect('draft_inbox')
    else:
        form = MessageForm()
    return render(request, 'send_message.html', {'form': form})



@login_required
def edit_message(request, message_id):
    """View to edit a message."""

    message = Message.objects.get(id=message_id)
    if request.user == message.sender:
        if request.method == 'POST':
            form = MessageForm(request.POST, instance=message)
            if form.is_valid():
                message = form.save(commit=False)

                if 'save_as_draft' in request.POST:
                    message.is_draft = True
                elif 'send' in request.POST:
                    message.is_draft = False

                message.save()

                if message.is_draft:
                    return redirect('draft_inbox')
                else:
                    return redirect('inbox')
        else:
            form = MessageForm(instance=message)
        return render(request, 'edit_message.html', {'form': form, 'message': message})
    else:
        # Handle unauthorized access
        pass


@login_required
def delete_message(request, message_id):
    """View to delete a message."""

    message = Message.objects.get(id=message_id)
    if request.user == message.sender:
        message.delete()
    return redirect('inbox')

def delete_selected_messages(request):
    """View to delete selected messages."""

    if request.method == 'POST':
        message_ids = request.POST.getlist('message_ids')
        Message.objects.filter(id__in=message_ids).delete()
    return redirect('inbox')

    