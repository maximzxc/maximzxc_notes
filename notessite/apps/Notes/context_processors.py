from models import Note


def count_notes(request):
    count = Note.objects.count()
    return {'count_notes': count, }
