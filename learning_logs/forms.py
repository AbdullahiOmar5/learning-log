from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """A form for creating new topics."""

    class Meta:
        model = Topic
        fields = ["text"]
        labels = {"text": ""} 
class EntryForm(forms.ModelForm):
    """A form for creating new entries."""
    
    class Meta:
        model = Entry
        fields = ["text"]
        labels = {"text": "Entry:"}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
