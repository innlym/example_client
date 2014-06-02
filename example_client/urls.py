from django.conf.urls import patterns, include, url
from accounts.views import *
from django.contrib import admin
import django.contrib.auth.views as authviews

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', authviews.logout, {'next_page': '/'}, name='logout'),
    url(r'^passport/$', passport, name='passport'),
    url(r'^$', profile, name='profile'),
)
