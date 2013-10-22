from django.conf.urls import patterns, url

from notessite.apps.Notes.views import NotesListView, search_form, search, add
from notessite.apps.Notes.views import RandomNote

urlpatterns = patterns('',
                       url(r'^search_form/$', search_form, name='search_form'),
                       url(r'^search/$', search, name='search'),
                       url(r'^add/$', add, name='add'),
                       url(r'^insert/$', RandomNote.as_view(), name='insert'),
                       url(r'^list/$', NotesListView.as_view(),
                           name="notes_list"))
