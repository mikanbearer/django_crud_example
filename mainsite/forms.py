from django import forms
from .models import Linkman

class LinkmanForm(forms.ModelForm):
    class Meta:
        model = Linkman
        fields = ('name', 'sex', 'tel', 'email')
        widgets = {
            'name': forms.TextInput(),
            'sex': forms.RadioSelect(),
            'tel': forms.TextInput(),
            'email': forms.EmailInput(),
        }