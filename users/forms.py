from django import forms
#from users.models import Restaurant, NGO
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField(required=True)
    #uid = forms.CharField(required=True)
    mobile = forms.CharField(required=True)
    address = forms.CharField(required=True)
    user_type = forms.ChoiceField(choices=(('R','Restaurant'),('N','NGO')), required=True)
    
    class Meta:
        model = User
        fields = ['name', 'user_type', 'mobile', 'email', 'address','username', 'password1','password2']


'''
class NGOForm(forms.ModelForm):
    class Meta:
        model = NGO
        password = forms.CharField(widget=forms.PasswordInput)
        confirm_password = forms.CharField(widget=forms.PasswordInput)
        fields = ['name', 'nid', 'mobile_no', 'email_id', 'address', 'password']
'''