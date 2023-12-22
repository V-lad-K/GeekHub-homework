# Автоматизувати процес замовлення робота за допомогою Selenium
# 1. Отримайте та прочитайте дані з
# "https://robotsparebinindustries.com/orders.csv". Увага! Файл має
# бути прочитаний з сервера кожного разу при запускі скрипта, не
# зберігайте файл локально.
# 2. Зайдіть на сайт "https://robotsparebinindustries.com/"
# 3. Перейдіть у вкладку "Order your robot"
# 4. Для кожного замовлення з файлу реалізуйте наступне:
#     - закрийте pop-up, якщо він з'явився. Підказка: не кожна кнопка
#     його закриває.
#     - оберіть/заповніть відповідні поля для замовлення
#     - натисніть кнопку Preview та збережіть зображення отриманого
#     робота. Увага! Зберігати треба тільки зображення робота, а не
#     всієї сторінки сайту.
#     - натисніть кнопку Order та збережіть номер чеку. Увага! Інколи
#     сервер тупить і видає помилку, але повторне натискання кнопки
#     частіше всього вирішує проблему. Дослідіть цей кейс.
#     - переіменуйте отримане зображення у формат <номер чеку>_robot
#     (напр. 123456_robot.jpg). Покладіть зображення в директорію
#     output (яка має створюватися/очищатися під час запуску скрипта).
#     - замовте наступного робота (шляхом натискання відповідної кнопки)
#
# ** Додаткове завдання (необов'язково)
#     - окрім збереження номеру чеку отримайте також HTML-код
#     всього чеку
#     - збережіть отриманий код в PDF файл
#     - додайте до цього файлу отримане зображення робота (бажано на
#     одній сторінці, але не принципово)
#     - збережіть отриманий PDF файл у форматі <номер чеку>_robot в
#     директорію output. Окремо зображення робота зберігати не потрібно.
#     Тобто замість зображень у вас будуть pdf файли які містять
#     зображення з чеком.
import csv
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from io import StringIO
from pathlib import Path

import requests
import os
import shutil


BASE_URL = "https://robotsparebinindustries.com/"
DIR_PATH = Path(__file__).resolve().parent / 'output'
SERVICE = ChromeService(ChromeDriverManager().install())
WIDTH_IMAGE = 342
HEIGHT_IMAGE = 200


class Robot:
    def __init__(self):
        self.file_path = DIR_PATH
        self.current_picture_path = None
        self.driver = webdriver.Chrome(service=SERVICE)
        self.driver.get(BASE_URL)
        self.remove_output()
        self.create_output()

    def remove_output(self):
        if os.path.exists(self.file_path):
            shutil.rmtree(self.file_path)

    def create_output(self):
        if not os.path.exists(self.file_path):
            os.makedirs(self.file_path)

    def redirect_to_order_your_robot(self):
        page_links = self.driver.find_elements(By.CLASS_NAME, "nav-link")
        order_your_robot_element = page_links[-1]
        order_your_robot_element.click()

    def wait_element(self, xpath_element):
        wait = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((
                    By.XPATH,
                    xpath_element
                )
            )
        )
        return wait

    def close_modal_window(self):
        xpath = "//button[@class='btn btn-danger' and text()='I guess so...']"

        close_button = self.wait_element(xpath)
        close_button.click()

    def build_order(self, data_arg):
        head_value = data_arg["Head"]
        body_value = data_arg["Body"]
        legs_value = data_arg["Legs"]
        address_value = data_arg["Address"]

        input_elements = self.driver.find_elements(By.CLASS_NAME, "form-control")

        head_element = self.driver.find_element(
            By.XPATH,
            f"//option[@value={head_value}]"
        )
        body_element = self.driver.find_element(
            By.XPATH,
            f"//input[@value={body_value}]/ancestor::label"
        )
        legs_element = input_elements[0]
        address_element = input_elements[1]

        head_element.click()
        body_element.click()
        legs_element.send_keys(legs_value)
        address_element.send_keys(address_value)

    def click_make_preview(self):
        while True:
            try:
                preview_button = self.driver.find_element(
                    By.XPATH,
                    f'//button[@id="preview"]'
                )
                self.driver.execute_script(
                    "arguments[0].click();",
                    preview_button
                )
                xpath = "//div[@id='robot-preview-image']"
                image = self.wait_element(xpath).find_element(By.XPATH, xpath)
                if image:
                    break
            except NoSuchElementException:
                break

    def click_make_order(self):
        while True:
            try:
                order_button = self.driver.find_element(
                    By.XPATH,
                    '//button[@id="order"]'
                )
                self.driver.execute_script(
                    "arguments[0].click();",
                    order_button
                )
            except NoSuchElementException:
                break

    def get_order_check(self):
        xpath = "//p[@class='badge badge-success']"
        check = self.wait_element(xpath)
        return check.find_element(By.XPATH, xpath).text

    def scroll_down(self):
        main_container_xpath = "//div[@class='container main-container']"
        main_container = self.driver.find_element(By.XPATH, main_container_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", main_container)

    def save_picture(self):
        self.scroll_down()

        xpath_element = "//div[@id='robot-preview-image']"
        check = self.get_order_check()
        file_name = f"output/{check}_robot.jpg"

        self.current_picture_path = str(Path(__file__)
                                        .resolve().parent / file_name)
        time.sleep(2)
        robot_photo = self.driver.find_element(By.XPATH, xpath_element)
        robot_photo.screenshot(file_name)
    
    def make_all_orders(self):
        data = self.get_data_orders(BASE_URL)
        for data_item in data:
            self.close_modal_window()
            self.build_order(data_item)
            self.click_make_preview()
            self.click_make_order()
            self.save_picture()
            self.click_another_robot()

    def click_another_robot(self):
        another_robot_button = self.driver.find_element(
            By.XPATH,
            "//button[@id='order-another']"
        )
        self.driver.execute_script("arguments[0].click();", another_robot_button)

    def start(self):
        self.redirect_to_order_your_robot()
        self.make_all_orders()

    @staticmethod
    def get_data_orders(url):
        csv_url = "orders.csv"
        request_url = url + csv_url
        response = requests.get(url=request_url)
        csv_reader = csv.DictReader(StringIO(response.text))

        return list(csv_reader)

    def __del__(self):
        self.driver.quit()


my_robot = Robot()
my_robot.start()
