from django.shortcuts import render, get_object_or_404
from .models import Post,Category,Tag
from .pagination import paginate_queryset


def home(request):
    posts = Post.objects.published().with_related().order_by("-published_at")

    page_obj = paginate_queryset(request,posts)

    return render(request, "blog/post_list.html", {"page_obj":page_obj})

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

    page_obj = paginate_queryset(request, posts)
    context = {
        "category":category,
        "page_obj":page_obj,

    }

    return render(request,"blog/category_posts.html", context)

def tag_posts(request,slug):

    tag = get_object_or_404(Tag,slug=slug)

    posts = tag.posts.published().with_related().order_by("-published_at")

    page_obj = paginate_queryset(request, posts)
    context ={
        "tag":tag,
        "page_obj":page_obj,
    }

    return render(request,"blog/tag_posts.html", context)



