from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.DecimalField(decimal_places=2, max_digits=10)


    def __str__(self):
        return self.product_name

class Sales(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    sale_date = models.DateField()
    product_quantity = models.IntegerField(default=0)
    unit_price = models.DecimalField(decimal_places=2, max_digits=10)
    total_price = models.IntegerField()

    def __str__(self):
        return product.product_name
