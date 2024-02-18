from django import forms
from .models import Note
from django_summernote.widgets import SummernoteWidget
class NoteForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Note
        fields = ['title', 'content']  # Adjust fields as needed
