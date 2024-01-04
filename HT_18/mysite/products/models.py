from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    short_description = models.TextField()
    brand_name = models.CharField(max_length=100)
    category = models.CharField(max_length=200)
    product_link = models.CharField(max_length=2000)
    product_id = models.URLField()

    def __str__(self):
        return self.name


class ScrapingTask(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
