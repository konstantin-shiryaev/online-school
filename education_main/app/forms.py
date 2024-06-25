from django import forms
from .models import Review
from manager.models import  Request

class CommentForm(forms.ModelForm):
    body = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'input', 'placeholder': 'Оставьте ваш отзыв'}
    ))
    
    class Meta:
        fields = ['body']
        model = Review
        
class RequestForm(forms.ModelForm):
    body = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'input', 'placeholder': 'Свяжитесь с нами'}
    ))
    class Meta:
        model = Request
        fields = ['body']