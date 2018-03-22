from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django import template

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})
	# return render(request, 'blog/post_kul.html', {'posts': posts})
