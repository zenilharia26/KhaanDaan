from django.urls import path
from django.conf.urls import url,include
from . import views

urlpatterns = [
    path('/user',views.dashboard,name='user-dashboard'),
]
