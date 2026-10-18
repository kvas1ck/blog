from django.shortcuts import render, get_object_or_404
from .models import Post


def home(request):
    posts = Post.objects.published()
    return render(request, "blog/home.html", {"posts":posts})

def about(request):
    return render(request,"blog/about.html")

def post_detail(request,slug):

    post = get_object_or_404(Post.objects.published().with_related(),slug=slug)

    context = {
        "post" : post
    }

    return render(request,"blog/post_detail.html", context)