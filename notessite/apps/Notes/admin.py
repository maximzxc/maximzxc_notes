from django.contrib import admin
from notessite.apps.Notes.models import Note
from notessite.apps.Notes.forms import NoteForm


class NoteAdmin(admin.ModelAdmin):
    form = NoteForm

admin.site.register(Note, NoteAdmin)
