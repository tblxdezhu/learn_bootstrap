from django.db import models
from django import forms


# Create your models here.

class Tester(models.Model):
    name = models.CharField(max_length=20)
    job = models.CharField(max_length=20)


class Process(models.Model):
    id = models.AutoField(primary_key=True)
    test_date = models.DateTimeField()
    test_mode = models.CharField(max_length=1, choices=(
        ('1', 'SLAM'),
        ('2', 'SSA'),
    ))
    test_data = models.CharField(max_length=20)
