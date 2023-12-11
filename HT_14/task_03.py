#  http://quotes.toscrape.com/ - написати скрейпер для збору всієї
#  доступної інформації про записи: цитата, автор, інфа про автора
#  тощо.
# - збирається інформація з 10 сторінок сайту.
# - зберігати зібрані дані у CSV файл

import requests
import csv
from bs4 import BeautifulSoup


def get_soup(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'lxml')
    return None


def get_born_and_description_by_name(data_list, author):
    if data_list:
        for item in data_list:
            if item[1] == author:
                return item[2], item[3]
    return False


def get_author_biography(link_author):
    response_biography = requests.get(link_author)
    if response_biography.status_code == 200:
        soup_biography = BeautifulSoup(response_biography.text, 'lxml')
        born_info = soup_biography.select_one('span.author-born-date').text
        description_info = soup_biography.select_one('div.author-description').text
        return born_info, description_info
    return None, None


def get_quotes():
    base_url = "https://quotes.toscrape.com/"
    data = [['quote', 'author', 'born', 'description']]

    while True:
        print(base_url)
        soup = get_soup(base_url)
        if not soup:
            break

        quote_titles = soup.select('div.quote')
        for quote in quote_titles:
            new_page_info = []
            quote_info = quote.select_one('span.text').text
            author_info = quote.select_one('small.author').text

            if not get_born_and_description_by_name(data, author_info):
                href_about_author = quote.find("a").get('href')
                link_author = f"https://quotes.toscrape.com/{href_about_author[1:]}"

                born_info, description_info = get_author_biography(link_author)
            else:
                born_info, description_info = get_born_and_description_by_name(data, author_info)

            new_page_info.extend([quote_info,
                                  author_info,
                                  born_info,
                                  description_info])
            data.append(new_page_info)

        next_li = soup.find('li', class_='next')
        if not next_li:
            break

        a_tag = next_li.find('a')
        href_a = a_tag.get('href')
        base_url = f"https://quotes.toscrape.com/{href_a[1:]}"

    return data


def save_csv_file(data_list):
    csv_file_path = 'data.csv'
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data_list)


scraped_data = get_quotes()
save_csv_file(scraped_data)
