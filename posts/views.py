from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Post


# Create your views here.
def post_detail(request, slug):
    template_name = "posts/detail.html"
    post = get_object_or_404(Post, slug=slug)
    context = {"post": post}
    return render(request, template_name, context)


def post_list(request):
    template_name = "posts/list.html"
    page = request.GET.get("page", 1)

    posts = Post.objects.filter(is_active=True)
    paginator = Paginator(posts, 12)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {"posts": posts}
    return render(request, template_name, context)


def post_search(request):
    template_name = "posts/search.html"
    query = request.GET.get("q", "")
    page = request.GET.get("page", 1)

    if query:
        posts = Post.objects.filter(is_active=True, title__icontains=query)
    else:
        posts = []

    paginator = Paginator(posts, 12)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {"posts": posts, "query": query}
    return render(request, template_name, context)
