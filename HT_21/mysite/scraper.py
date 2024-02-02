import requests
from urllib.parse import urljoin


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
        price = data["salePrice"]
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
