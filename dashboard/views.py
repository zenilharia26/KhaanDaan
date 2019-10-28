from django.shortcuts import render, redirect
from users.models import KhaanDaanUsers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from dashboard.forms import AddFood
from dashboard.models import Food

@login_required
def dashboard(request):
    user = KhaanDaanUsers.objects.get(user=request.user)
    return render(request, 'dashboard/dashboard.html', {'user':user})

@login_required
def profile(request):
    user = KhaanDaanUsers.objects.get(user=request.user)
    return render(request, 'dashboard/user.html', {'user':user})

@login_required
def table_list(request):
    user = KhaanDaanUsers.objects.get(user=request.user)
    food = Food.objects.all()
    return render(request, 'dashboard/tables.html', {'user':user, 'food':food})

@login_required
def typography(request):
    user = KhaanDaanUsers.objects.get(user=request.user)
    return render(request, 'dashboard/typography.html', {'user':user})

@login_required
def icons(request):
    user = KhaanDaanUsers.objects.get(user=request.user)
    return render(request, 'dashboard/icons.html', {'user':user})

@login_required
def map(request):
    user = KhaanDaanUsers.objects.get(user=request.user)
    return render(request, 'dashboard/map.html', {'user':user})

@login_required
def notifications(request):
    user = KhaanDaanUsers.objects.get(user=request.user)
    return render(request, 'dashboard/notifications.html', {'user':user})

@login_required
def add_food(request):
    user = KhaanDaanUsers.objects.get(user=request.user)
    if user.user_type == 'N':
        return redirect('dashboard')
    if request.method == 'POST':
        food = Food()
        food.restaurant = user
        food.name = request.POST.get("name","")
        food.food_type = request.POST.get("food_type","")
        food.quantity = request.POST.get("quantity","")
        food.save()
        return redirect('dashboard')
    else:
        form = AddFood()
    
    return render(request, 'dashboard/food.html', {'form':form})
        