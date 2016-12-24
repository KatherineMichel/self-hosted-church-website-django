from django.conf.urls import include, url
from django.views.generic.base import TemplateView
from django.contrib import admin

urlpatterns = [
    url(r'^activities/$', TemplateView.as_view(template_name="activities.html")),
    url(r'^about/$', TemplateView.as_view(template_name="about.html")),
    url(r'^admin/', admin.site.urls),
]


