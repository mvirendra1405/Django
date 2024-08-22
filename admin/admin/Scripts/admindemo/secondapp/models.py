from django.db import models

# Create your models here.
class Client(models.Model):
    c_name=models.CharField(max_length=30)
    c_email=models.CharField(max_length=30)
    c_contact=models.CharField(max_length=30)
    c_age=models.IntegerField()
    c_address=models.TextField(max_length=300)



    def __str__(self):
        return self.c_name