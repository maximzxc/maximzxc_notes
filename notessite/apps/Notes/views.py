# Create your views here.
from django.views.generic import ListView
from models import Note


class NotesListView(ListView):

    context_object_name = "notes_list"
    template_name = "notes/list.html"
    #queryset = Note.objects.order_by("added")
    paginate_by = 10

    def get_queryset(self):
            return Note.objects.order_by("added")
