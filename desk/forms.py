from django import forms

from desk.models import Desk


class DeskForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Desk
