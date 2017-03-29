from django.conf.urls import patterns, include, url
from django.contrib import admin

import calc.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^(\d+)([\+\-\/\*])(\d+)', calc.views.operaciones, name = 'calculadora'),
    url(r'^admin/', include(admin.site.urls)),
)
