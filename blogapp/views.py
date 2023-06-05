from django.shortcuts import render, get_object_or_404
from django.contrib.postgres.search import SearchVector
from django.http import Http404
from .models import Post
from django.core.paginator import Paginator, EmptyPage
from .forms import EmailPostForm, SearchForm

# Create your views here.


# List view
def post_list(request):
    post_list = Post.published.all()
    # Pagination with 6 posts per page
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get("page", 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "blogapp/post/list.html", {"posts": posts})


# Detail view of individual blog


def post_detail(request, post):
    post_list = Post.published.all()[:5]
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post)
    return render(
        request, "blogapp/post/detail.html", {"post": post, "post_list": post_list}
    )


# Email Form View
def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    if request.method == "Post":
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

    else:
        form = EmailPostForm()

    return render(request, "blogapp/post/share.html", {"post": post, "form": form})


# Search form view


def post_search(request):
    form = SearchForm()
    query = None
    results = []

    if "query" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            results = Post.published.annotate(
                search=SearchVector("title", "body"),
            ).filter(search=query)

    return render(
        request,
        "blogapp/post/search.html",
        {"form": form, "query": query, "results": results},
    )
