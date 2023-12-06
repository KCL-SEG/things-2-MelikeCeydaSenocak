from django import forms
from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity'] 

    widgets = {
        'description': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'maxlength': 120}),  
        'quantity': forms.NumberInput(attrs={'min': 0, 'max': 50}),  
    }
