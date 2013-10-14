from django.conf.urls import patterns, include, url
from notessite.apps.Notes.views import home

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
                       (r'^notes/', include('notessite.apps.Notes.urls')),
                       url(r'^$', home, name='home'),
                       (r'^admin/', include(admin.site.urls)))
