from django.db import models


class Product(models.Model):
    name = models.TextField()
    price = models.TextField()
    #short_description = models.TextField()
    brand_name = models.TextField()
    category = models.TextField()
    product_link = models.TextField()
    product_id = models.TextField()

    def __str__(self):
        return self.name


class ScrapingTask(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name
