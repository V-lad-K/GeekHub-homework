import sys
import os
import django
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from urllib.parse import urljoin
from products.models import Product, ScrapingTask

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


def get_unique_names_from_scraping_task():
    unique_name_list = set()
    model_names = ScrapingTask.objects.values_list('name', flat=True)
    for model_name in model_names:
        name_list = model_name.split(", ")
        unique_name_list.update(name_list)

    return list(unique_name_list)


def save_task(product_id_arg):
    existing_tasks = ScrapingTask.objects.filter(name=product_id_arg)
    if not existing_tasks.exists():
        ScrapingTask.objects.create(name=product_id_arg)


def save_product(product_id_arg):
    name_list = product_id_arg.split(", ")
    unique_names = get_unique_names_from_scraping_task()

    for name in name_list:
        data_scraper_fixed = get_product_data(product_id_arg)

        if data_scraper_fixed is not None:
            if name in unique_names:
                existing_product = Product.objects.get(product_id=name)

                existing_product.name = data_scraper_fixed["name"]
                existing_product.price = data_scraper_fixed["price"]
                existing_product.brand_name = data_scraper_fixed["brand_name"]
                existing_product.category = data_scraper_fixed["category"]
                existing_product.product_link = data_scraper_fixed["product_link"]
                existing_product.short_description = data_scraper_fixed["short_description"]

                existing_product.save()
            else:
                Product.objects.create(
                    name=data_scraper_fixed["name"],
                    price=data_scraper_fixed["price"],
                    short_description=data_scraper_fixed["short_description"],
                    brand_name=data_scraper_fixed["brand_name"],
                    category=data_scraper_fixed["category"],
                    product_link=data_scraper_fixed["product_link"],
                    product_id=data_scraper_fixed["product_id"],
                )


product_id = sys.argv[1]

save_product(product_id)
save_task(product_id)
