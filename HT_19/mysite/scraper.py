import sys
import os
import django
import requests

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
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


def save_task(product_id_arg):
    ScrapingTask.objects.update_or_create(name=product_id_arg)


def save_product(product_id_arg):
    name_list = product_id_arg.split(", ")

    for _ in name_list:
        scraper_data = get_product_data(product_id_arg)

        if scraper_data is not None:
            Product.objects.update_or_create(
                name=scraper_data["name"],
                price=scraper_data["price"],
                short_description=scraper_data["short_description"],
                brand_name=scraper_data["brand_name"],
                category=scraper_data["category"],
                product_link=scraper_data["product_link"],
                product_id=scraper_data["product_id"],
            )


product_id = sys.argv[1]

save_product(product_id)
save_task(product_id)
