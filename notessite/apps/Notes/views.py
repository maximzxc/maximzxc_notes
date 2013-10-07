# Create your views here.

from models import Note

def notes_list(request):

	return object_list(request.
			queryset=Note.objects.all(),
			template_name='apps/Notes/templates/notes.html',
			template_objects_name='note'
	)
