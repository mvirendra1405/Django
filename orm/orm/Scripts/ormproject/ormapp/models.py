from django.db import models

# Create your models here.
class emp(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    contact=models.CharField(max_length=30)
    age=models.IntegerField()
    address=models.TextField(max_length=300)

    class Meta:
        db_table='empp'


from django import forms

class empform(forms.ModelForm):
    class Meta:
        model=emp
        fields='__all__'
    

