from django.forms import ModelForm, CharField, Textarea
from models import Note


class NoteForm(ModelForm):
    content = CharField(
        min_length=10, widget=Textarea(attrs={'cols': 18, 'rows': 5}),
        required=True)
    title = CharField(max_length=255, required=True)

    class Meta:
        model = Note
        fields = ('title', 'content')
