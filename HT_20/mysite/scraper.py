import sys
import os
import django
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from urllib.parse import urljoin
from products.models import Product
from products.models import ScrapingTask
from products.models import Category


USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
              "(KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
BASE_URL = "https://www.sears.com/"


def get_product_data(product_id_arg: str):
    url = f"{BASE_URL}api/sal/v3/products/details/{product_id_arg}"
    headers = {
        "Authorization": "SEARS",
        "User-Agent": USER_AGENT
    }
    params = {
        'storeName': 'Sears',
        "memberStatus": "G",
        "zipCode": 10101,
    }

    response = requests.get(
        url=url,
        headers=headers,
        params=params
    )
    if response.status_code == 200:
        data = response.json()["productDetail"]["softhardProductdetails"][0]
        name = data["descriptionName"]
        price = data["price"]["finalPrice"]
        brand_name = data["brandName"]
        product_link = urljoin(BASE_URL, data["seoUrl"])
        category = data["hierarchies"]["specificHierarchy"][0]["name"]
        product_info = {
            "name": name,
            "price": price,
            "brand_name": brand_name,
            "category": category,
            "product_link": product_link,
            "product_id": product_id_arg
        }

        try:
            short_description = data["shortDescription"]
        except KeyError:
            short_description = ""

        product_info["short_description"] = short_description
        return product_info
    return


def save_task(product_ids_arg):
    product_ids_list = product_ids_arg.split(", ")
    for id_product in product_ids_list:
        ScrapingTask.objects.update_or_create(name=id_product)


def save_product_and_category(product_ids_arg):
    product_ids_list = product_ids_arg.split(", ")
    for id_product in product_ids_list:
        scraper_data = get_product_data(id_product)
        if scraper_data is not None:
            category_name = scraper_data["category"]
            category, _ = Category.objects.get_or_create(name=category_name)

            search_fields = {'product_id': id_product}
            defaults_data = {
                'name': scraper_data["name"],
                'price': scraper_data["price"],
                "short_description": scraper_data["short_description"],
                "brand_name": scraper_data["brand_name"],
                "category_id": category,
                "product_link": scraper_data["product_link"],
            }
            Product.objects.update_or_create(
                defaults=defaults_data,
                **search_fields
            )


product_id = sys.argv[1]
save_product_and_category(product_id)
save_task(product_id)
