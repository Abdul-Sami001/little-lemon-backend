from django.db import models


# Create your models here.
class Menue(models.Model):
    name = models.CharField(max_length=100)
    fname = models.CharField(max_length=20)


class Drink_Categories(models.Model):
    drink_category = models.CharField(max_length=100)


class Drinks(models.Model):
    drink_name = models.CharField(max_length=100)
    price = models.DecimalField
    drink_category = models.ForeignKey(Drink_Categories(), on_delete=models.CASCADE)


def __str__(self):
    return self.name + self.fname
