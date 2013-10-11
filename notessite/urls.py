from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from views import home

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import views

urlpatterns = patterns('',
                       (r'^notes/', include('notessite.apps.Notes.urls')),
                       url(r'^$', home, name='home'),
                       (r'^admin/', include(admin.site.urls)))
urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
