# Створіть програму для отримання курсу валют за певний період.
# - отримати від користувача дату (це може бути як один день так і
# інтервал - початкова і кінцева дати, продумайте механізм реалізації)
# і назву валюти
# - вивести курс по відношенню до гривні на момент вказаної дати
# (або за кожен день у вказаному інтервалі)
# - не забудьте перевірку на валідність введених даних

from datetime import datetime, timedelta
import requests


class InvalidDate(Exception):
    pass


def receive_exchange_rate(currency, start_date_str, end_date_str=None):
    date_now = datetime.today()
    start_date = datetime.strptime(start_date_str, "%d.%m.%Y")
    end_date = start_date

    if end_date_str is not None:
        end_date = datetime.strptime(end_date_str, "%d.%m.%Y")
    if start_date > date_now:
        raise InvalidDate("the start date cannot be in the future")

    if start_date > end_date:
        raise InvalidDate("start date must be before")
    days_count = (end_date - start_date).days

    for day in range(days_count + 1):
        new_date = (start_date + timedelta(days=day)).strftime("%d.%m.%Y")
        response = requests.get(f"https://api.privatbank.ua/p24api/exchange_rates?date={new_date}")
        exchange_rate_list = response.json()["exchangeRate"]

        if not exchange_rate_list:
            raise InvalidDate("the data has not been updated yet")

        print("date is ", new_date)
        for rate in exchange_rate_list:
            if rate["currency"] == currency:
                print(rate["currency"])
                print(f"PrivatBank's sales rate: {rate['saleRate']}")
                print(f"PrivatBank's purchase price: {rate['purchaseRate']}")


try:
    start_date_input = input("input start date like day.month.year: ")
    end_date_input = input("input end date like day.month.year: ")
    currency_input = input("input currency like USD: ")
    if not end_date_input:
        end_date_input = None

    receive_exchange_rate(currency_input, start_date_input, end_date_input)
except InvalidDate as e:
    print(str(e))
except ValueError as e:
    print(str(e))
