from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input', 'placeholder': 'Оставьте ваш отзыв'}
    ))
    
    class Meta:
        fields = ['body']
        model = Review