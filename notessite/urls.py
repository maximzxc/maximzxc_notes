from django.conf.urls import patterns, include, url
from notessite.apps.Notes.views import home

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()


urlpatterns = patterns('',
                       (r'^notes/', include('notessite.apps.Notes.urls')),
                       url(r'^$', home, name='home'),
                       (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.MEDIA_ROOT}),
                       (r'^admin/', include(admin.site.urls)))
