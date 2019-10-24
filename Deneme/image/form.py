from django import forms
from .models import home


class fileForm(forms.ModelForm):
    class Meta:
        model = home
        fields = [
            'file',
            'email',
            'comment',
        ]
