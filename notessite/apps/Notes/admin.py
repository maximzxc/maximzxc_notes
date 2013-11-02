from django.contrib import admin
from notessite.apps.Notes.models import Note, Book
from notessite.apps.Notes.forms import NoteForm


class NoteAdmin(admin.ModelAdmin):
    form = NoteForm

admin.site.register(Note, NoteAdmin)
admin.site.register(Book)
