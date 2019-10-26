from django import forms
from users.models import Restaurant, NGO

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        password = forms.CharField(widget=forms.PasswordInput)
        confirm_password = forms.CharField(widget=forms.PasswordInput)
        fields = ['name', 'rid', 'mobile_no', 'email_id', 'address', 'password']

class NGOForm(forms.ModelForm):
    class Meta:
        model = NGO
        password = forms.CharField(widget=forms.PasswordInput)
        confirm_password = forms.CharField(widget=forms.PasswordInput)
        fields = ['name', 'nid', 'mobile_no', 'email_id', 'address', 'password']
