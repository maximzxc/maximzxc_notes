from django.conf.urls import patterns

from views import NotesListView

urlpatterns = patterns('',
                       (r'^list/$', NotesListView.as_view()))
