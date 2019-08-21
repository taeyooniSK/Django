from django.shortcuts import render
from django.utils import timezone
from .models import Post  # '.'는 현재 디렉토리(= './')를 뜻함
# Create your views here.


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
