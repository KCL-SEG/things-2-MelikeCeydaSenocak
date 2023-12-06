from django import forms
from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        exclude = ['created_at']  # To exclude 'created_at' field from the form

    # You can customize field widgets here if needed
    widgets = {
        'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),  # Display description as Textarea
        'quantity': forms.NumberInput(attrs={'min': 0, 'max': 50}),  # Display quantity as NumberInput
    }
