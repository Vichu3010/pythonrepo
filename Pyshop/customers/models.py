from django.db import models


class Customers(models.Model):
    Id = models.IntegerField(max_length=10)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    contact = models.IntegerField(10)
    address = models.CharField(max_length=255)

