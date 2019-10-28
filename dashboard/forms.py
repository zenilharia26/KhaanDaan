from django import forms
from django.contrib.auth.models import User
from dashboard.models import Food

class AddFood(forms.ModelForm):
    name = forms.CharField(max_length=50)
    food_type = forms.CharField(max_length=50)
    quantity = forms.FloatField(required=True)
    class Meta:
        model = Food
        fields = ['name', 'food_type', 'quantity']