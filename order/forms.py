from django import forms
from .models import Order, lay, Roll

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class LayForm(forms.ModelForm):
    class Meta:
        model = lay
        fields = '__all__'

class RollForm(forms.ModelForm):
    class Meta:
        model = Roll
        fields = '__all__'
