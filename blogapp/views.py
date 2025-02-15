from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .forms import CommentForm
from .models import Post, Comment
# Create your views here.

def post_list(request):
    post_list = Post.published.all()
    # pagination with limited posts per page
    paginator = Paginator(post_list, 2)
    page_number = request.GET.get('page', 1)
    posts = paginator.page(page_number)
    return render(request, 'blogapp/post/list.html', {'posts':posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post, publish__year=year, publish__month=month, publish__day=day)
    
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('blogapp:post_detail', year=year, month=month, day=day, post=post.slug)
    else:
        form = CommentForm()
    return render(request, 'blogapp/post/detail.html', {'post':post, 'comments':comments, 'form':form})


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED) 
    comment = None 
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request, 'blogapp/post/detail.html', {'posts':posts, 'form':form, 'comment':comment})  