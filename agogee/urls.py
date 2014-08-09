from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from agogee import views

urlpatterns = patterns("",
	url(r'^$', views.index, name='index'),
	url(r'^spartanMain', TemplateView.as_view(template_name='agogee/spartanMain.html'), name='spartanMain'),
	url(r'^events', TemplateView.as_view(template_name='agogee/events.html'), name='events'),
	url(r'^community', TemplateView.as_view(template_name='agogee/community.html'), name='community'),
	url(r'^profile', TemplateView.as_view(template_name='agogee/profile.html'), name='profile'),
	url(r'^register', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^profile/$', views.profile, name='profile'),
	url(r'^thankyou/$', TemplateView.as_view(template_name='agogee/thankyou.html'), name='thankyou'),
)
