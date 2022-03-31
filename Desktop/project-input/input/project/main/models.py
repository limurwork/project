from django.db import models
from django.db import connections
# Create your models here.



class EmployeeDetails(models.Model):
    Contract = models.CharField(max_length=124)
    subject_contract = models.CharField(max_length=124)
    date_contract = models.CharField(max_length=124)
    end_contract = models.CharField(max_length=124)
    href_cloud = models.CharField(max_length=124)
    class Meta:
        db_table = 'contract'


class Mart(models.Model):
    Addres_Hause = models.CharField(max_length=124)
    Namber_Apartmens = models.CharField(max_length=124)
    ownership = models.CharField(max_length=124)
    Name = models.CharField(max_length=124)
    Date_Of_Birth = models.CharField(max_length=124)
    Place_Of_Birth = models.CharField(max_length=124)
    Dokument_Right = models.CharField(max_length=124)
    personal_account = models.CharField(max_length=124)
    Size_Apartment = models.CharField(max_length=124)

    class Meta:
        db_table = 'contract2'