from django.db import models
from users.models import KhaanDaanUsers
from django.contrib.auth.models import User

class Food(models.Model):
    restaurant = models.ForeignKey(KhaanDaanUsers, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False)
    food_type = models.CharField(max_length=50)
    quantity = models.FloatField(null=False)
    served_to = models.CharField(max_length=50)
# Create your models here.
