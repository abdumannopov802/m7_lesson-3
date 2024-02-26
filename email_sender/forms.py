from django import forms
from .models import MyModle

class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModle
        fields = ['field1', 'field2']