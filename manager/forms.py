from django import forms

from manager.models import Manager


class ManagerForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Manager