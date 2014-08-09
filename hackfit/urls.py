from django.conf.urls import patterns, include, url
from django.conf import settings

from posts.views import PostListView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hackfit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^agogee/', include('agogee.urls', namespace='agogee')),

    url(r'^$', PostListView.as_view(), name='home'),
)

if settings.DEBUG:
	urlpatterns += patterns(
		'django.views.static',
		(r'media/(?P<path>.*)',
			'serve',
			{'document_root': settings.MEDIA_ROOT}),
		)
