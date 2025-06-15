from django.db import models
from  django.contrib.auth.models import User
# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_no = models.CharField(max_length=10)
    class Types(models.TextChoices):
        SAVINGS = 'Savings'
        CURRENT = 'Current'
    account_type = models.CharField(max_length=8, choices=Types.choices, default=Types.SAVINGS)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)

    def __str__(self):
        return str(self.account_no)
    
class Demographics(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    identification = models.CharField("NID / Birth Certificate #", max_length=99)
    class Genders(models.TextChoices):
        MALE = 'Male'
        FEMALE = 'Female'
        OTHER = 'Other'
    gender = models.CharField(max_length=10, choices=Genders.choices)
    birth_date = models.DateField(null=True, blank=True)
    street_address = models.CharField(max_length=99)
    city = models.CharField(max_length= 99)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=99)

    def __str__(self):
        return str(self.user.email)