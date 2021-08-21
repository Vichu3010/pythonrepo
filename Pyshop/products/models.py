from django.db import models


class Products (models.Model):
    name=models.CharField(max_length=255)
    price=models.FloatField()
    stock=models.IntegerField()
    image_urls=models.CharField(max_length=2084)


class Offer(models.Model):
    code=models.CharField(max_length=10)
    description=models.CharField(max_length=255)
    discount=models.FloatField()


