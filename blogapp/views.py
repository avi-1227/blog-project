from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(status=Post.Status.PUBLISHED)
    return render(request, 'blogapp/post/list.html',{'posts':posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'blogapp/post/detail.html',{'post':post})

def about(request):
    return render(request, 'blogapp/post/about.html')

def contact(request):
    return render(request, 'blogapp/post/contact.html')