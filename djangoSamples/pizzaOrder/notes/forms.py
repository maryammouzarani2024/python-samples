from django import forms 
from django.core.exceptions import ValidationError

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model= Notes
        fields= ('title', 'text')
        widgets= {
            'title': forms.TextInput(attrs={'class':'form-control my-5'}),
            'text':forms.Textarea(attrs={'class':'form-control mb-5'})
        }
        labels={
            'text':'Write your thoughts here',
        }
    
    def clean_text(self):
        text=self.cleaned_data['text'].lower()
        if 'pizza' not in text: 
            raise ValidationError("We only accept notes about pizza")
        return text