from django.shortcuts import render,redirect
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
    if request.method == 'POST':
        # user.name = request.POST.get("name","")
        # user.email_id = request.POST.get("email_id","")
        # user.mobile_no = request.POST.get("mobile_no","")
        # user.address = request.POST.get("address","")
        # user.save()
        post = request.POST
        KhaanDaanUsers.objects.filter(user=request.user).update(name=post.get("name",""), email_id=post.get("email_id",""), mobile_no=post.get("mobile_no",""), address=post.get("address",""))
    user = KhaanDaanUsers.objects.get(user=request.user)
    return render(request, 'dashboard/user.html', {'user':user})

@login_required
def table_list(request):
    user = KhaanDaanUsers.objects.get(user=request.user)
    food=Food.objects.all()

    if request.method == 'POST':
        food_req = Food.objects.get(id=request.POST.get("food_id",""))
        food_req.delete()
        return redirect('dashboard-table-list')
    if user.user_type=='N':
        return render(request, 'dashboard/tables.html', {'user':user,'food':food})
    else:
        return redirect('dashboard')
        
@login_required
def typography(request):
    user = KhaanDaanUsers.objects.get(user=request.user)
    return render(request, 'dashboard/typography.html', {'user':user})


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
        print(request)
        print(request.POST)
        food = Food()
        food.restaurant = user
        food.name = request.POST.get("name","")
        food.food_type = request.POST.get("food_type","")
        food.quantity = request.POST.get("quantity","")
        food.save()
        return redirect('dashboard-add-food')
    else:
        form = AddFood()
    
    return render(request, 'dashboard/food.html', {'form':form, 'user':user})
        