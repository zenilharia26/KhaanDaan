from django.db import models

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    rid = models.IntegerField(primary_key=True)
    mobile_no = models.CharField(max_length=10,null=False, unique=True)
    email_id = models.EmailField(max_length=100, null=False)
    address = models.CharField(max_length=200, null=False)
    password = models.CharField(max_length=50, null=False)

class NGO(models.Model):
    name = models.CharField(max_length=50)
    nid = models.IntegerField(primary_key=True)
    mobile_no = models.CharField(max_length=10,null=False, unique=True)
    email_id = models.EmailField(max_length=100, null=False)
    address = models.CharField(max_length=200, null=False)
    password = models.CharField(max_length=50, null=False)
