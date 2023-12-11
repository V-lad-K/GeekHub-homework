# Використовуючи Scrapy, заходите на
# "https://chrome.google.com/webstore/sitemap", переходите на кожен лінк
# з тегів <loc>, з кожного лінка берете посилання на сторінки
# екстеншенів, парсите їх і зберігаєте в CSV файл ID, назву та короткий
# опис кожного екстеншена (пошукайте уважно де його можна взяти)

import scrapy
from scrapy import Request
from scrapy.http import Response
from bs4 import BeautifulSoup


class GoogleSpider(scrapy.Spider):
    name = "google"
    allowed_domains = ["chrome.google.com"]
    start_urls = ["https://chrome.google.com/webstore/sitemap"]

    def parse(self, response: Response, **kwargs):
        soup = BeautifulSoup(response.text, "xml")
        locs = soup.select("loc")

        for loc in locs:
            yield Request(
                url=loc.text,
                callback=self.parse_url
            )

    def parse_url(self, response: Response):
        soup = BeautifulSoup(response.text, "xml")
        locs = soup.select("loc")

        for loc in locs:
            yield Request(
                url=loc.text,
                callback=self.parse_site_extension
            )

    @staticmethod
    def parse_site_extension(response: Response):

        id_ = (response.css('[property="og:url"]::attr(content)')
               .get()
               .split('/')
               .pop())
        yield {
            'id': f'{id_}',
            'name': response.css('[property="og:title"]::attr(content)').get(),
            'brief_description':
                response.css('[property="og:description"]::attr(content)').get()
        }
