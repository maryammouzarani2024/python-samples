from django import forms
from .models import Pizza, Size

class PizzaForm(forms.ModelForm):
    class Meta:
        model=Pizza
        fields=['topping1', 'topping2', 'size','title', 'image']
        labels={'topping1':'Topping 1', 'topping2': 'Topping 2'}
