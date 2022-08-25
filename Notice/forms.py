from dataclasses import field
import imp
from pyexpat import model
from tkinter.ttk import Widget
from django.forms import ModelForm
from.models import Comment
from django import forms

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields =(
                    'aothor',
                    'notice',
                    'body'
                )
        widgets = {
            'aothor': forms.TextInput( attrs={'class': 'form-control','value':'','id':'aothor','type':'hidden'}),
            'notice': forms.TextInput( attrs={'class': 'form-control','value':'', 'id':'notice','type':'hidden'}),
            'body': forms.TextInput( attrs={'class': 'form-control','placeholder':'Write your comment..'}),
        }
      