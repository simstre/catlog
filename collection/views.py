from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


def post_list(request, username=None):
    if username:
        try:
            uid = User.objects.get(username=username).pk
            posts = Post.objects.filter(created_date__lte=timezone.now(), user=uid).order_by('last_updated')
        except ObjectDoesNotExist:
            posts = None
    else:
        posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('last_updated')
    return render(request, 'collection/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'collection/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.last_updated = timezone.now
            post.save()
            return redirect('collection.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'collection/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('collection.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'collection/post_edit.html', {'form': form})