from django import forms
from django.contrib.auth.models import User
from .models import Customer, OrderRecords
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from phonenumber_field.formfields import PhoneNumberField


class UserSignupForm(UserCreationForm):
  

     class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email')

class CustomerSignupForm(forms.ModelForm):
    phone = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': ('+12345678899')}), label=("Phone number"), required=False)
    class Meta:
        model =   Customer
        
        fields = ('address', 'post_code', 'phone', 'profile_photo',)


class OrderEditForm(forms.ModelForm):

    class Meta:
        model= OrderRecords
        fields= ( 'extra_topping1', 'extra_topping2',)