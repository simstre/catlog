from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(last_updated__lte=timezone.now()).order_by('last_updated')
    return render(request, 'collection/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'collection/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'collection/post_edit.html', {'form': form})