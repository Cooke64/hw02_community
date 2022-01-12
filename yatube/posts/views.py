from django.shortcuts import render, get_object_or_404

from .models import Post, Group

# Количество постов для показа
AMOUNT_POST = 10


def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    posts = Post.objects.order_by('-pub_date')[:AMOUNT_POST]
    context = {
        'posts': posts,
        'title': title,
        'text': 'Главная страница',
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Записи сообщества'
    group = get_object_or_404(Group, slug=slug)
    get_posts = Post.objects.filter(group=group)
    posts = get_posts.order_by('-pub_date')[:AMOUNT_POST]
    context = {
        'title': title,
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
