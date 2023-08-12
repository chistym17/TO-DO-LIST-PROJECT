from django import forms
from app1.models import taskmodel

class task_form(forms.ModelForm):
    class Meta:
        model=taskmodel
        fields=['task_title','task_description']        
       