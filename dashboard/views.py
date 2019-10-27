from django.shortcuts import render
from users.models import Restaurant,NGO
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

@login_required
def profile(request):
    return render(request, 'dashboard/user.html')

@login_required
def table_list(request):
    return render(request, 'dashboard/tables.html')

@login_required
def typography(request):
    return render(request, 'dashboard/typography.html')

@login_required
def icons(request):
    return render(request, 'dashboard/icons.html')

@login_required
def map(request):
    return render(request, 'dashboard/map.html')

@login_required
def notifications(request):
    return render(request, 'dashboard/notifications.html')