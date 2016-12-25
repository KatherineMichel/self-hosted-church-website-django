from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def blog(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog.html', {'posts': posts})
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post-detail.html', {'post': post})

