from django import forms

DISPLAY_CHOICES = (
    ("Power Saver", "Power Saver"),
    ("Normal", "Normal")
)

class MyForm(forms.Form):
    display_type = forms.ChoiceField(widget=forms.RadioSelect, choices=DISPLAY_CHOICES)