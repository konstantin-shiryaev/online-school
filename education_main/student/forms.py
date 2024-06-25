from django import forms
from .models import *

class CheckForm(forms.ModelForm):
    file = forms.FileField()

    class Meta:
        model = Check
        fields = ['file']
