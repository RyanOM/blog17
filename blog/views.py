from django.shortcuts import render
from .models import Post


# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
	#return render(request, 'blog/post_list.html', {'posts': posts})
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug=""):
	try:
		post = Post.objects.get(slug=slug.lower())
	except Post.DoesNotExist:
		return render(request, 'blog/base.html')
	return render(request, 'blog/post_detail.html', {
		'post': post,
	})

def posts_by_tag(request, slug=""):
	posts = Post.objects.filter(tags__slug=slug.lower())
	#if posts.count() == 0:
	#	raise Exception("whatever")
	return render(request, 'blog/post_list.html', {'posts': posts, 'slug': slug})