from django.db import models

# Create your models here.


class NID(models.Model):
    name = models.CharField(max_length=100, null=False)
    father_name = models.CharField(max_length=100, null=False)
    mother_name = models.CharField(max_length=100)
    present_address = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=100)
    nid_number = models.IntegerField()

    def __str__(self):
        return self.name

class DrivingLicence(models.Model):
    nid = models.OneToOneField(NID, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    l_num = models.IntegerField(verbose_name="Licence Number")
    def __str__(self):
        return self.name
