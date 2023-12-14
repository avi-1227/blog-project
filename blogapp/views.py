from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
from django.views.decorators.http import require_POST

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(status=Post.Status.PUBLISHED)
    return render(request, 'blogapp/post/list.html',{'posts':posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    # List of active comments for this post
    comments = post.comments.filter(active=True)
    # Form for users to comment
    form = CommentForm()
    return render(request, 'blogapp/post/detail.html',{'post':post ,'comments': comments, 'form': form})

def about(request):
    return render(request, 'blogapp/post/about.html')

def contact(request):
    return render(request, 'blogapp/post/contact.html')


# Comment View
@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post=post
        comment.save()
    return render(request, 'blogapp/post/comment.html', {'post': post, 'form': form, 'comment': comment})
