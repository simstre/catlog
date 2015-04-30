from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(last_updated__lte=timezone.now()).order_by('last_updated')
    return render(request, 'collection/post_list.html', {'posts': posts})
