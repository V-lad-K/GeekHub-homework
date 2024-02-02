<<<<<<< HEAD
import json
import sys
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()


from products.models import Product
from products.models import Category


def update_product(default_data_arg, product_id_arg, category_arg):
    category, _ = Category.objects.get_or_create(name=category_arg)
    search_fields = {'product_id': product_id_arg}
    Product.objects.update_or_create(
        defaults=default_data_arg,
        **{"category_id": category},
        **search_fields
    )


product_id = sys.argv[1]
default_data = json.loads(sys.argv[2])
category = sys.argv[3]
update_product(default_data, product_id, category)
=======
import json
import sys
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()


from products.models import Product
from products.models import Category


def update_product(default_data_arg, product_id_arg, category_arg):
    category, _ = Category.objects.get_or_create(name=category_arg)
    search_fields = {'product_id': product_id_arg}
    Product.objects.update_or_create(
        defaults=default_data_arg,
        **{"category_id": category},
        **search_fields
    )


product_id = sys.argv[1]
default_data = json.loads(sys.argv[2])
category = sys.argv[3]
update_product(default_data, product_id, category)
>>>>>>> 970411dd3de5ed996f005820fcc60d8b4bc41da5
