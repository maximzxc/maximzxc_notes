from django import template
from Notes.models import Note
register = template.Library()


@register.inclusion_tag("search.html")
def search(id):
    try:
        search = Note.objects.get(pk=id)
    except Note.DoesNotExist:
        search = None
    return {'Note': search}
