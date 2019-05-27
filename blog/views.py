from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required


def list(request):
    posts = Post.objects.order_by('created_date')
    return render(request, 'postlist.html', {'posts': posts})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'postdetail.html', {'post': post})

@login_required
def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/blog/')

    return render(request, 'postedit.html')

@login_required
def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/blog/')

    return render(request, 'postedit.html', {'post' : post})

@login_required
def commentlist(request):
    posts = Post.objects.order_by('created_date')
    return render(request, 'commentadd.html', {'posts': posts})

@login_required
def remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('/blog/')

@login_required
def commentadd(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            print(request.path)
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(request.path.replace('comment/', ''))
    return render(request, 'commentadd.html')