from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from taggit.models import Tag

from .models import Post

#local functions
def _paginate_posts(request, posts):
	paginator = Paginator(posts, 3)
	#providing page with current
	page = request.GET.get('page', 1)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return posts

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
	#return render(request, 'blog/post_list.html', {'posts': posts})
	paginated = _paginate_posts(request, posts)
	return render(request, 'blog/post_list.html', {
		'posts': paginated,
		'tags': Tag.objects.all(),
	})

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
	paginated = _paginate_posts(request, posts)
	return render(request, 'blog/post_list.html', {
		'posts': paginated,
		'slug': slug,
		'tags': Tag.objects.all(),
	})