from logging.config import _LoggerConfiguration
from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = models.Charfield(max_length=100)
    photo_url = models.Textfield(max_length=200)

    def __str__(self):
        return self.start_year


class Donut(models.Model):
    shop = models.ForeignKey(
        Shop, on_delete=models.CASCADE, related_name='donuts')
    name = models.CharField(max_length=100)
    details = models.TextField(max_length=200, default='no detials')
    image_url = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.name