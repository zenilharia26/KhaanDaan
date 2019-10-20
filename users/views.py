from django.shortcuts import render
from users.forms import RestaurantForm, NGOForm
# Create your views here.

def register_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RestaurantForm()
    return render(request, 'users/register.html', {'form':form, 'name':'Restaurant'})

def register_ngo(request):
    if request.method == 'POST':
        form = NGOForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NGOForm()
    return render(request, 'users/register.html', {'form':form, 'name':'NGO'})