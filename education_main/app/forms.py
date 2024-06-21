from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    body = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'input', 'placeholder': 'Оставьте ваш отзыв'}
    ))
    
    class Meta:
        fields = ['body']
        model = Review