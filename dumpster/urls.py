from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from publisher import urls

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'dumpster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^article/', include(urls)),
    url(r'^admin/', include(admin.site.urls)),
) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
