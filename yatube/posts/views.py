from django.shortcuts import get_object_or_404, render
from .models import Group, Post


POSTS_ON_PAGE = 10


def index(request):
    # Главная страница
    template = 'posts/index.html'
    posts = Post.objects.select_related('group')[:POSTS_ON_PAGE]
    context = {
        'posts': posts
    }
    return render(request, template, context)


def group_posts(request, slug):
    # Страница группы
    group_template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.select_related(
        'group').filter(group=group)[:POSTS_ON_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, group_template, context)
