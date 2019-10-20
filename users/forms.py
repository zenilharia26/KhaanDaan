from django import forms
from users.models import Restaurant, NGO

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'mobile_no', 'email_id', 'address']

class NGOForm(forms.ModelForm):
    class Meta:
        model = NGO
        fields = ['name', 'mobile_no', 'email_id', 'address']
