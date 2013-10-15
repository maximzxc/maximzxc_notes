from django import template
from notessite.apps.Notes.models import Note
register = template.Library()


@register.inclusion_tag("search.html")
def search(id):
    search = Note.objects.get(pk=id)
    return {'Note': search}
