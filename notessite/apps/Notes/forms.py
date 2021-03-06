from django.forms import ModelForm, CharField, ImageField
from widgets import BetterTextarea
from models import Note


class NoteForm(ModelForm):
    content = CharField(min_length=10, widget=BetterTextarea(), required=True)
    title = CharField(max_length=255, required=True)
    image = ImageField(required=True)

    class Meta:
        model = Note
        fields = ('title', 'content', 'image')
