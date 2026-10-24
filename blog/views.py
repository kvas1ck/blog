from django.shortcuts import render, get_object_or_404
from .models import Post,Category,Tag


def home(request):
    posts = Post.objects.published()
    return render(request, "blog/post_list.html", {"posts":posts})

def about(request):
    return render(request,"blog/about.html")

def post_detail(request,slug):

    post = get_object_or_404(Post.objects.published().with_related(), slug=slug)
    
    context = {
        "post" : post
    }

    return render(request,"blog/post_detail.html", context)


def category_posts(request,slug):

    category = get_object_or_404(Category,slug=slug)

    posts = category.posts.published().with_related().order_by("-published_at")

    context = {
        "category":category,
        "posts":posts
    }

    return render(request,"blog/category_posts.html", context)

def tag_posts(request,slug):

    tag = get_object_or_404(Tag,slug=slug)

    posts = tag.posts.published().with_related().order_by("-published_at")

    context ={
        "tag":tag,
        "posts":posts
    }

    return render(request,"blog/tag_posts.html", context)

