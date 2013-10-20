# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import ListView
from notessite.apps.Notes.models import Note
from django.http import HttpResponse
from django.shortcuts import render
from notessite.apps.Notes.forms import NoteForm
from django.utils import simplejson


def home(request):

    return render_to_response(
        'base.html', {}, context_instance=RequestContext(request))


def search_form(request):

    return render_to_response(
        'notes/search_form.html', {}, context_instance=RequestContext(request))


def add(request):

    if request.method == 'POST' and request.is_ajax():
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(
                simplejson.dumps({'response': ("Note was added"),
                                  'result': 'success'}),
                mimetype='application/json')
        else:
            response = {}
            for k in form.errors:
                response[k] = form.errors[k][0]
            return HttpResponse(
                simplejson.dumps({'response': response,
                                  'result': 'error'}),
                mimetype='application/json')
    else:
        form = NoteForm()
    return render(request, 'notes/add.html', {'form': form})


def search(request):

    if 'id' in request.GET and request.GET['id']:
        id = request.GET['id']
        if id.isdigit():
            return render(request, 'notes/search.html', {'id': id})
        else:
            return HttpResponse('Please submit a search term with integer.')
    else:
        return HttpResponse('Please submit a search term.')


class NotesListView(ListView):

    context_object_name = "notes_list"
    template_name = "notes/list.html"
    paginate_by = 10

    def get_queryset(self):
        return Note.objects.order_by("-updated")
