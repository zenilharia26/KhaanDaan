from django.shortcuts import render
from users.models import KhaanDaanUsers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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
    return render(request, 'dashboard/tables.html', {'user':user})

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