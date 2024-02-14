from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Category name")

    def __str__(self):
        return self.name


class Goods(models.Model):
    name = models.CharField(max_length=200, verbose_name="Goods name")
    description = models.CharField(max_length=200, verbose_name="Goods description")
    price = models.IntegerField(verbose_name="Goods price")
    category = models.ForeignKey(Category, related_name="goods", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
