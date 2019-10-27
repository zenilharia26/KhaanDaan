from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages
from users.models import KhaanDaanUsers
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('name')
            khaan_user = KhaanDaanUsers()
            khaan_user.user = User.objects.get(email=form.cleaned_data.get('email'))
            khaan_user.name = form.cleaned_data.get('name')
            khaan_user.mobile_no = form.cleaned_data.get('mobile')
            khaan_user.email_id = form.cleaned_data.get('email')
            khaan_user.address = form.cleaned_data.get('address')
            khaan_user.user_type = form.cleaned_data.get('user_type')
            khaan_user.save()
            messages.success(request,f'Account created successfully for {username}!')
            return redirect('login')

    else:
        form = UserRegisterForm()

        
    return render(request, 'users/register.html', {'form':form, 'name':'Restaurant'})

def register_restaurant(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('name')
            restaurant = KhaanDaanUsers()
            restaurant.user = User.objects.get(email=form.cleaned_data.get('email'))
            restaurant.name = form.cleaned_data.get('name')
            #restaurant.uid = form.cleaned_data.get('uid')
            restaurant.mobile_no = form.cleaned_data.get('mobile')
            restaurant.email_id = form.cleaned_data.get('email')
            restaurant.address = form.cleaned_data.get('address')
            restaurant.user_type = form.cleaned_data.get('user_type')
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
            ngo = KhaanDaanUsers()
            ngo.user = User.objects.get(email=form.cleaned_data.get('email'))
            ngo.name = form.cleaned_data.get('name')
            #ngo.uid = form.cleaned_data.get('uid')
            ngo.mobile_no = form.cleaned_data.get('mobile')
            ngo.email_id = form.cleaned_data.get('email')
            ngo.address = form.cleaned_data.get('address')
            ngo.user_type = form.cleaned_data.get('user_type')
            ngo.save()
            messages.success(request,f'Account created successfully for {username}!')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form, 'name':'NGO'})
