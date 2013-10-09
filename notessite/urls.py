from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

import views

urlpatterns = patterns('',
                       (r'^notes/', include('notessite.apps.Notes.urls')),
                       url(r'^$', views.home, name='home'),
                       (r'^admin/', include(admin.site.urls))) + static(
settings.STATIC_URL, document_root=settings.STATIC_ROOT)
