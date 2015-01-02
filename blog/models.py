from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	slug = models.SlugField(max_length=200, unique=True)
	tags = TaggableManager()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null =True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __unicode__(self):
		return self.title

	@models.permalink
	def get_absolute_url(self):
		return ('blog_post_view_detail', None, {'slug': self.slug})
