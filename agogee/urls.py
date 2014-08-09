from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView
from agogee import views

urlpatterns = patterns("",
	url(r'^$', TemplateView.as_view(template_name='agogee/spartanMain.html'), name='index'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),)