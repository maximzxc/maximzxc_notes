# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import ListView
from notessite.apps.Notes.models import Note


def home(request):

    return render_to_response(
        'base.html', {}, context_instance=RequestContext(request))


def search_form(request):

    return render_to_response(
        'notes/search_form.html', {}, context_instance=RequestContext(request))


def search(request):

    return render_to_response(
        'notes/search.html', {}, context_instance=RequestContext(request))


class NotesListView(ListView):

    context_object_name = "notes_list"
    template_name = "notes/list.html"
    paginate_by = 10

    def get_queryset(self):
        return Note.objects.order_by("added")
