from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Employee(models.Model):
    usern = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, unique=True)
    name = models.CharField(max_length=200, null=False)
    mobile = models.IntegerField(null=False)
    desig_choice = (
        ('cleaner','Cleaner'),
        ('treasurer ','Treasurer'),
    )
    designation = models.CharField(choices=desig_choice, max_length=50)

    def __str__(self):
        return self.name
