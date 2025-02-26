from .models import BikeModel
from django import forms

class BikeForm(forms.ModelForm):
    class Meta:
        model=BikeModel
        fields='__all__'
