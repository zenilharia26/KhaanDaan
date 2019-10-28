from django.urls import path
from django.conf.urls import url,include
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='dashboard-user-profile'),
    path('tablelist/', views.table_list, name='dashboard-table-list'),
    path('typography/', views.typography, name='dashboard-typography'),
    path('map/', views.map, name='dashboard-map'),
    path('notifications/', views.notifications, name='dashboard-notifications'),
    path('addfood/', views.add_food, name='dashboard-add-food')
]
