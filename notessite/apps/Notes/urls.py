from django.conf.urls.defaults import *

import views

urlpatterns = patterns('',

		url(r'^list/$', views.notes_list, name = 'notes_list'),
)
