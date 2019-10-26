from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages
from users.models import Restaurant, NGO
from django.contrib.auth.models import User

# Create your views here.

def register_restaurant(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('name')
            restaurant = Restaurant()
            restaurant.user = User.objects.get(email=form.cleaned_data.get('email'))
            restaurant.name = form.cleaned_data.get('name')
            restaurant.rid = form.cleaned_data.get('user_id')
            restaurant.mobile_no = form.cleaned_data.get('mobile')
            restaurant.email_id = form.cleaned_data.get('email')
            restaurant.address = form.cleaned_data.get('address')
            restaurant.save()
            messages.success(request,f'Account created successfully for {username}!')
            return redirect('login')

    else:
        form = UserRegisterForm()

        
    return render(request, 'users/register.html', {'form':form, 'name':'Restaurant'})

def register_ngo(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('name')
            ngo = NGO()
            ngo.user = User.objects.get(email=form.cleaned_data.get('email'))
            ngo.name = form.cleaned_data.get('name')
            ngo.nid = form.cleaned_data.get('user_id')
            ngo.mobile_no = form.cleaned_data.get('mobile')
            ngo.email_id = form.cleaned_data.get('email')
            ngo.address = form.cleaned_data.get('address')
            ngo.save()
            messages.success(request,f'Account created successfully for {username}!')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form, 'name':'NGO'})
