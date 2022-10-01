from django import forms
from .models import Record

class RecordModelForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['author', 'email', 'body']
        widgets = {
            'author':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Автор'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'example@example.com'}),
            'body':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Введите текст'}),
        }