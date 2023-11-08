from django import forms
from .models import*

class user_form(forms.ModelForm):
    class Meta:
        model = user_data
        fields = '__all__'

class cart_form(forms.ModelForm):
    class Meta:
        model = cart
        fields = '__all__'