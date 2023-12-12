# Викорисовуючи requests, написати скрипт, який буде приймати на вхід ID
# категорії із сайту https://www.sears.com і буде збирати всі товари із
# цієї категорії, збирати по ним всі можливі дані (бренд, категорія,
# модель, ціна, рейтинг тощо) і зберігати їх у CSV файл (наприклад, якщо
# категорія має ID 12345, то файл буде називатись 12345_products.csv)

import csv
import requests
import time


ITEM_COUNT = 48
DELAY = 20
BASE_URL = "https://www.sears.com/api/sal/v3/products/search"
USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
              "(KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")

data = [['brand', 'category', 'model', 'price']]


def get_data(category_id_argument, start_index_arg, end_index_arg):
    new_data = []
    params = {
        'searchType': 'category',
        'catalogId': 12605,
        'store': 'Sears',
        "storeId": 10153,
        "catGroupId": category_id_argument,
        "startIndex": start_index_arg,
        "endIndex": end_index_arg,
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
            brand = item["brandName"]
            model = item["name"]
            price = item["additionalAttributes"]["sellPrice"]
            new_data.append([brand, model, price, category])
        return new_data
    return


def save_csv_file(data_argument, name_file):
    with open(name_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data_argument)


def save_data(category_id_arg, start_index_arg, end_index_arg):
    all_data = [['brand', 'category', 'model', 'price']]

    while True:
        time.sleep(DELAY)
        start_index_arg += ITEM_COUNT
        end_index_arg += ITEM_COUNT

        new_data = get_data(category_id_arg, start_index_arg, end_index_arg)
        if new_data is None:
            break
        all_data.extend(new_data)
        save_csv_file(all_data, name_file_csv)


try:
    category_id = int(input("input category_id: "))
    start_index = 1
    end_index = 48

    name_file_csv = str(category_id) + "_products.csv"
    save_data(category_id, start_index, end_index)
except ValueError:
    print("category_id must be integer")
