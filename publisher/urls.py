from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^(?P<article_id>.+)$', views.get_article),
)
