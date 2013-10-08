# Create your views here.
from django.views.generic.list_detail import object_list

from models import Note

def notes_list(request):

	return object_list(request,
			queryset = Note.objects.all(),
			template_name = 'notes/list.html',
			template_object_name = 'note'
	)
