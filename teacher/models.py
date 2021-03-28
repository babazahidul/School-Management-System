from django.db import models

# Create your models here.


class Teacher(models.Model):
    name = models.CharField(max_length=200, null=False)
    gender_choice = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )
    gender = models.CharField(choices=gender_choice, max_length=200, null=False)
    phone = models.IntegerField()
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.name
