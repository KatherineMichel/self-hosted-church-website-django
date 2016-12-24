from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from django.contrib import admin

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name="home.html")),
    url(r'^activities/$', TemplateView.as_view(template_name="activities.html")),
    url(r'^about/$', TemplateView.as_view(template_name="about.html")),
    url(r'^children-and-youth-ministries/$', TemplateView.as_view(template_name="detail-pages/children-and-youth-ministries.html")),
    url(r'^church/$', TemplateView.as_view(template_name="detail-pages/church.html")),
    url(r'^community-outreach/$', TemplateView.as_view(template_name="detail-pages/community-outreach.html")),
    url(r'^global-church/$', TemplateView.as_view(template_name="detail-pages/global-church.html")),
    url(r'^music-ministry/$', TemplateView.as_view(template_name="detail-pages/music-ministry.html")),
    url(r'^pretty-prairie/$', TemplateView.as_view(template_name="detail-pages/pretty-prairie.html")),
    url(r'^united-methodist-women/$', TemplateView.as_view(template_name="detail-pages/united-methodist-women.html")),
    url(r'^welcome/$', TemplateView.as_view(template_name="detail-pages/welcome.html")),
    url(r'^worship/$', TemplateView.as_view(template_name="detail-pages/worship.html")),
    url(r'^admin/', admin.site.urls),
]




