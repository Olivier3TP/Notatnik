from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'author', 'status']
class EditNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'author', 'status']