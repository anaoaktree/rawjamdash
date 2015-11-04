from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', hello.views.index, name='index'),
    url(r'^tables/', hello.views.tables, name='tables'),
    url(r'^bigTable/', hello.views.bigTable, name='bigtables'),
    url(r'^admin/', include(admin.site.urls)),
)