from django.http import Http404
from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, slug):
    try:
        post = Post.published.get(
            slug=slug,
            publish__year=year,
            publish__month=month,
            publish__day=day
        )
    except Post.DoesNotExist:
        raise Http404("No Post Found")

    return render(request, 'blog/post/detail.html', {'post': post})
