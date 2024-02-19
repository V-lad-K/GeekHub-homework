from celery import shared_task

from products.models import Product
from products.models import Category


@shared_task
def update_product(default_data_arg, product_id_arg, category_arg):
    category, _ = Category.objects.get_or_create(name=category_arg)
    search_fields = {'product_id': product_id_arg}
    Product.objects.update_or_create(
        defaults=default_data_arg,
        **{"category_id": category},
        **search_fields
    )
