# -*- coding: utf-8 -*-
#
# Copyright (c) 2010 Cidadanía Coop.
# Written by: Oscar Carballal Prego <info@oscarcp.com>
#
# This file is part of e-cidadania.
#
# e-cidadania is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# e-cidadania is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with e-cidadania. If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    # Django administration
    (r'^admin/', include(admin.site.urls)),

    # User accounts
    #(r'^accounts/', include('apps.accounts.urls')),
    #(r'^accounts/', include('apps.registration.urls')),
    
    (r'^/(?P<space>)/', include('apps.spaces.urls')),
    
    (r'^accounts/', include('apps.userprofile.urls')),
    
    (r'^proposals/', include('apps.proposals.urls')),
    
    
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'static'}),

)

# If DEBUG=True in settings.py add static content served by django.
#if settings.DEBUG:
#    urlpatterns += ('',
#    
#    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
#        {'document_root': 'static'}),
#    
#    )
