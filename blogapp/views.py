from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post
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
    return render(request, 'blogapp/post/detail.html', {'post':post})
    