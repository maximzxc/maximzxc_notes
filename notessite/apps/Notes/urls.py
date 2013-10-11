from django.conf.urls import patterns, url

from notessite.apps.Notes.views import NotesListView

urlpatterns = patterns('',
                       url(r'^list/$', NotesListView.as_view(),
                           name="notes_list"))
