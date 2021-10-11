from django import forms
from .models import Water

class WaterForm(forms.ModelForm):
    drinking = forms.BooleanField(required=False, label="mark if you drinking water")
    class Meta:
        model = Water
        fields=['drinking']