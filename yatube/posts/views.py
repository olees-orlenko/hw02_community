from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
from .models import Group, Post
# Create your views here.


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'Последние обновления на сайте'
    text = 'Последние обновления на сайте'
    context = {
        'title': title,
        'posts': posts,
        'text': text,
    }
    return render(request, 'posts/index.html', context)
    #template = 'posts/index.html'
    #return render(request, template, context)
    #return HttpResponse('Главная страница')

def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    title = (f'Записи сообщества {group.title}')
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/group_list.html', context) 
    #template = 'posts/group_list.html'
    #return HttpResponse(f'Список постов {any_slug}')
    #return render(request, template, context)
