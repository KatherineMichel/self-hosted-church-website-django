from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.blog, name='blog'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post-detail'),
]

