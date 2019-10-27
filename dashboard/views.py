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

def maps(request):
    return render(request, 'dashboard/maps.html')

def notifications(request):
    return render(request, 'dashboard/icons.html')