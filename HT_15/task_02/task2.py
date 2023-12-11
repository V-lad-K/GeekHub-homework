# Викорисовуючи requests, заходите на ось цей сайт
# "https://www.expireddomains.net/deleted-domains/"
# (з ним будьте обережні), вибираєте будь-яку на ваш вибір доменну зону
# і парсите список  доменів - їх там буде десятки тисяч
# (звичайно ураховуючи пагінацію). Всі отримані значення зберігти в CSV
# файл.

import csv
import requests
import time
from bs4 import BeautifulSoup


BASE_URL = "https://member.expireddomains.net/domains/expiredcom/"
LOGIN_CHECK_URL = "https://www.expireddomains.net/logincheck/"
USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
              "(KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
DELAY = 15


def get_session_header():
    login_data = {
        'login': 'Vladic',
        'password': '19732846vK'
    }
    header_data = {'User-Agent': USER_AGENT}
    session_data = requests.Session()

    session_data.post(LOGIN_CHECK_URL, data=login_data, headers=header_data)
    return session_data, header_data


def get_page_domain(start, session_arg, header_arg):
    params = {"start": start}
    response = session_arg.get(url=BASE_URL, headers=header_arg, params=params)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        tds = soup.select("td.field_domain")
        domain_list_on_page = []
        if not tds:
            print("need login")
            return []
        for td in tds:
            domain_list_on_page.append(td.a.text)

        return domain_list_on_page


def get_all_domains(session_arg, header_arg):
    data = ['Domain']
    start = 0
    page_count = 0
    while True:
        print(f"Page{page_count}")
        time.sleep(DELAY)
        get_data = get_page_domain(start, session_arg, header_arg)
        data.extend(get_data)
        save_csv_file(data)
        if not get_data:
            return
        start += 25
        page_count += 1


def save_csv_file(data_argument):
    name_file_csv = "domains.csv"

    with open(name_file_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for data in data_argument:
            writer.writerow([data])


session, header = get_session_header()
get_all_domains(session, header)
