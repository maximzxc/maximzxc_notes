from django.conf.urls import patterns, url

from notessite.apps.Notes.views import search_form, search

urlpatterns = patterns('',
                       url(r'^search_form/$', search_form, name='search_form'),
                       url(r'^search/$', search, name='search'))
