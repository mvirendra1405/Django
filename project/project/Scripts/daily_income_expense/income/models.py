from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class income(models.Model):
    income=models.IntegerField()
    income_type=models.CharField(max_length=30)
    income_date=models.DateField()
    description=models.TextField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)


    class Meta:
        db_table='income'

from django import forms
class incomeform(forms.ModelForm):
    class Meta:
        model=income
        fields='__all__'