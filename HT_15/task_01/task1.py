# Викорисовуючи requests, написати скрипт, який буде приймати на вхід ID
# категорії із сайту https://www.sears.com і буде збирати всі товари із
# цієї категорії, збирати по ним всі можливі дані (бренд, категорія,
# модель, ціна, рейтинг тощо) і зберігати їх у CSV файл (наприклад, якщо
# категорія має ID 12345, то файл буде називатись 12345_products.csv)

import csv
import requests


class InvalidIdCategory(Exception):
    pass


BASE_URL = "https://www.sears.com/api/sal/v3/products/search"
USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
              "(KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")


def get_data(category_id_argument):
    data = [['brand', 'category', 'model', 'price']]
    params = {
        "storeId": 10153,
        "catGroupId": category_id_argument,
    }
    response = requests.get(
        url=BASE_URL,
        headers={"Authorization": "SEARS", "User-Agent": USER_AGENT},
        params=params,
    )

    if response.status_code == 200:
        items = response.json()["items"]
        product_hierarchy = response.json()["productHierarchy"][0]
        category = product_hierarchy["categoryName"]

        for item in items:
            new_data = []
            brand = item["brandName"]
            model = item["name"]
            price = item["additionalAttributes"]["sellPrice"]
            new_data.extend([brand, category, model, price])
            data.append(new_data)
        return data

    raise InvalidIdCategory("category id does not exist")


def save_csv_file(data_argument, name_file):
    if data_argument is None:
        raise InvalidIdCategory("")

    with open(name_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data_argument)


try:
    category_id = input("Enter category id: ")
    name_file_csv = str(category_id) + "_products.csv"
    data = get_data(category_id)
    save_csv_file(data, name_file_csv)
except InvalidIdCategory as e:
    print(str(e))
