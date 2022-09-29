from random import choices
from django.db import models

GENDER_CHOICES = (("F", "Female"), ("M", "Male"))


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
