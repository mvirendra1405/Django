from django.db import models
from firstapp.models import Emp
from secondapp.models import Client
# Create your models here.
class Project(models.Model):
    project_name=models.CharField(max_length=30)
    project_status=models.CharField(max_length=30)
    emp=models.ForeignKey(Emp,on_delete=models.CASCADE)
    client=models.ForeignKey(Client,on_delete=models.CASCADE)