from django.forms import ModelForm
from django import forms
from .models import DataBase


class EntryForm (ModelForm):
    class Meta:
        model = DataBase
        fields = ['name','designation','section']
        widgets = {
            'name': forms.TextInput(attrs = {'class' : 'form-control'}),
            'designation': forms.TextInput(attrs = {'class' : 'form-control'}),
            'section': forms.TextInput(attrs = {'class' : 'form-control'}),
        }