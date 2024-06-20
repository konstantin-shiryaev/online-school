from django import forms
from .models import *

class UserQuestionForm(forms.ModelForm):
    body = forms.CharField(label='', widget=forms.Textarea(
        attrs={'class': 'UserQuestion', 'placeholder': 'Оставьте ваш вопрос'}
    ))
    
    class Meta:
        fields = ['body']
        model = UserQuestion