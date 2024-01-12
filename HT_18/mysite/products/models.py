from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(max_length=100)
    short_description = models.TextField()
    brand_name = models.CharField(max_length=100)
    category = models.CharField(max_length=200)
    product_link = models.URLField()
    product_id = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ScrapingTask(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
