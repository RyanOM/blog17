from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
		url(r'^blog$', views.post_list),

		url(r'^blog/tag/(?P<slug>[^\.]+)$', views.posts_by_tag, name='blog_posts_by_tag'),
		
		url(r'^blog/(?P<slug>[^\.]+)$', views.post_detail, name='blog_post_view_detail'),

)