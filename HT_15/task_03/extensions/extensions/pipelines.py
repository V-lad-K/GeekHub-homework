# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import csv


class GoogleExtensionPipeline:
    @staticmethod
    def process_item(item, spider):
        with open('data_extensions.csv', "a", newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=['id', 'name', 'brief_description'])
            csv_writer.writerow(item)
        return item
