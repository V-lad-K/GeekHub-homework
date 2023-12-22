import csv
import requests
from io import StringIO

#
# def read_csv_from_request(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()  # Перевірка на помилки під час отримання даних
#
#         # Читання CSV даних з реквеста
#         csv_data = response.text
#
#         # Ініціалізація читача CSV
#         csv_reader = csv.DictReader(StringIO(csv_data))
#         print("csv_reader", csv_reader)
#         # Конвертація даних у список словників
#         data = list(csv_reader)
#
#         return data
#     except requests.RequestException as e:
#         print("Помилка під час обробки запиту:", e)
#         return None
#
# # Приклад використання методу для читання CSV з реквеста
# url = 'https://robotsparebinindustries.com/orders.csv'  # Замініть це посиланням на ваш CSV файл
# csv_data = read_csv_from_request(url)
#
# if csv_data is not None:
#     # Використання отриманих даних (csv_data) для подальшої обробки
#     print(csv_data)
# else:
#     print("Не вдалося отримати дані з реквеста")





import csv
import requests
import io

url = 'https://robotsparebinindustries.com/orders.csv'
r = requests.get(url)
r.encoding = 'utf-8'  # useful if encoding is not sent (or not sent properly) by the server
csvio = io.StringIO(r.text, newline="")
data = []
for row in csv.DictReader(csvio):
    data.append(row)

print(data)