from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.auth import views as auth_views

admin.autodiscover()

import hello.views

urlpatterns = patterns('',
    url(r'^$', hello.views.index, name='index'),
    #url(r'^login/', auth_views.login, name='login'),
    url(r'^tables/', hello.views.tables, name='tables'),
    url(r'^bigTable/', hello.views.bigTable, name='bigtables'),
    #url(r'^authentication/', hello.views.authentication, name='authentication'),
    url(r'^admin/', include(admin.site.urls)),
)