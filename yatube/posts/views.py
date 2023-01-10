from django.shortcuts import render, get_object_or_404

from .models import Group, Post

QUANTITY = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:QUANTITY]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:QUANTITY]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
