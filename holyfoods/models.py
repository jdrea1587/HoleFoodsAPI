from django.db import models

# Create your models here.


class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    photo_url = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Donut(models.Model):
    shop = models.ForeignKey(
        Shop, on_delete=models.CASCADE, related_name='donuts')
    name = models.CharField(max_length=100, default='no name')
    details = models.CharField(max_length=100, default='no details')
    image_url = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.name
