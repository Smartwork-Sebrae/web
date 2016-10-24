from django import forms

from manager.models import Manager


class ManagerForm(forms.ModelForm):
    class Meta:
        fields = ('hour', 'produced', 'order')
        widgets = {
            'hour': forms.TimeInput(format='%H:%M'),
        }
        model = Manager