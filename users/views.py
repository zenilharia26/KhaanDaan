from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.

def register_restaurant(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('name')
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
            username=form.cleaned_data.get('name')
            messages.success(request,f'Account created successfully for {username}!')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form, 'name':'NGO'})
