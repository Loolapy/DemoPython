from django import forms
from .models import movie

class Movieform(forms.ModelForm):
    class Meta:
        model=movie
        fields=['name','dec','Year','img']
