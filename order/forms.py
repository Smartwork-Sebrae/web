from django import forms

from order.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Order
