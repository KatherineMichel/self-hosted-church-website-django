from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name="home.html"), name="home"),    
    url(r'^welcome/$', TemplateView.as_view(template_name="detail-pages/welcome.html"), name="welcome"),
    url(r'^worship/$', TemplateView.as_view(template_name="detail-pages/worship.html"), name="worship"),
    url(r'^global-church/$', TemplateView.as_view(template_name="detail-pages/global-church.html"), name="global-church"),
    url(r'^music-ministry/$', TemplateView.as_view(template_name="detail-pages/music-ministry.html"), name="music-ministry"),
    url(r'^church/$', TemplateView.as_view(template_name="detail-pages/church.html"), name="church"),
    url(r'^children-and-youth-ministries/$', TemplateView.as_view(template_name="detail-pages/children-and-youth-ministries.html"), name="children-and-youth-ministries"),
    url(r'^united-methodist-women/$', TemplateView.as_view(template_name="detail-pages/united-methodist-women.html"), name="united-methodist-women"),
    url(r'^community-outreach/$', TemplateView.as_view(template_name="detail-pages/community-outreach.html"), name="community-outreach"),
    url(r'^pretty-prairie/$', TemplateView.as_view(template_name="detail-pages/pretty-prairie.html"), name="pretty-prairie"),                    
    url(r'^activities/$', TemplateView.as_view(template_name="activities.html"), name="activities"),
    # url(r'^blog/$', TemplateView.as_view(template_name="blog.html"), name="blog"),
    # url(r'^blog/$,' include('blog.urls')),
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name="about"),
    url(r'^blog/$', views.blog, name='blog'),
    url(r'^admin/', admin.site.urls),
]




