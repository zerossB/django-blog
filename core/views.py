from django.shortcuts import render
from posts.models import Post


# Create your views here.
def index(request):
    template_name = "index.html"
    posts = Post.objects.filter(is_active=True)[:4]
    context = {"posts": posts}
    return render(request, template_name, context)
