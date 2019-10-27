from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def profile(request):
    return render(request, 'dashboard/user.html')

def table_list(request):
    return render(request, 'dashboard/tables.html')

def typography(request):
    return render(request, 'dashboard/typography.html')

def icons(request):
    return render(request, 'dashboard/icons.html')

def map(request):
    return render(request, 'dashboard/map.html')

def notifications(request):
    return render(request, 'dashboard/notifications.html')