from django import forms
from .models import Order, lay

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class LayForm(forms.ModelForm):
    class Meta:
        model = lay
        fields = '__all__'
