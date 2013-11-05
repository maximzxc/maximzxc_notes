# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import ListView
from Notes.models import Note
from django.http import HttpResponse
from django.shortcuts import render
from Notes.forms import NoteForm


def home(request):
    '''
    home page
    '''
    return render_to_response(
        'base.html', {}, context_instance=RequestContext(request))


def search_form(request):
    '''
    page for searching
    contains search form
    '''
    return render_to_response(
        'notes/search_form.html', {}, context_instance=RequestContext(request))


def add(request):
    '''
    page for adding notes
    it checks if request method is POST and if form is valid
    in this case it save it and reload page
    in other case it just reload page and show errors
    '''
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            text = 'Note was successfully created'
        else:
            form = NoteForm()
            text = ''
        return render(request, 'notes/add.html', {'form': form,
                                                  'text': text})
    else:
        form = NoteForm()
        text = ''
    return render(request, 'notes/add.html', {'form': form,
                                              'text': text})


def search(request):
    '''
    after sending search form this page start working
    it checks if form is valid and if it is shows note that you need
    '''
    if 'id' in request.GET and request.GET['id']:
        id = request.GET['id']
        if id.isdigit():
            return render(request, 'notes/search.html', {'id': id})
        else:
            return HttpResponse('Please submit a search term with integer.')
    else:
        return HttpResponse('Please submit a search term.')


class NotesListView(ListView):
    '''
    show list of exist notes
    '''
    context_object_name = "notes_list"
    template_name = "notes/list.html"
    paginate_by = 10

    def get_queryset(self):
        return Note.objects.order_by("added")
