from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class KhaanDaanUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=10,null=False, unique=True)
    email_id = models.EmailField(max_length=100, null=False)
    address = models.CharField(max_length=200, null=False)
    user_type = models.CharField(max_length=20, choices=[('R','Restaurant'),('N','NGO')])
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')
