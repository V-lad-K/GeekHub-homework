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

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
from io import BytesIO
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
        self.current_picture = None
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
        head_value = data_arg[0]
        body_value = data_arg[1]
        legs_value = data_arg[2]
        address_value = data_arg[3]

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
        try:
            while True:
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
        except Exception:
            pass

    def click_make_order(self):
        try:
            while True:
                order_button = self.driver.find_element(
                    By.XPATH,
                    '//button[@id="order"]'
                )
                self.driver.execute_script(
                    "arguments[0].click();",
                    order_button
                )
        except Exception:
            pass

    def get_order_check(self):
        xpath = "//p[@class='badge badge-success']"
        check = self.wait_element(xpath)
        return check.find_element(By.XPATH, xpath).text

    def make_picture(self, data_arg):
        head_value = data_arg[0]
        body_value = data_arg[1]
        legs_value = data_arg[2]

        image_urls = [
            f"https://robotsparebinindustries.com/heads/{head_value}.png",
            f"https://robotsparebinindustries.com/bodies/{body_value}.png",
            f"https://robotsparebinindustries.com/legs/{legs_value}.png"
        ]

        images = []
        for url in image_urls:
            response = requests.get(url)

            img = Image.open(BytesIO(response.content))
            img_resized = img.resize((HEIGHT_IMAGE, HEIGHT_IMAGE))
            images.append(img_resized)

        widths, heights = zip(*(i.size for i in images))
        combined_image = Image.new('RGB', (max(widths), sum(heights)))

        y_offset = 0
        for img in images:
            combined_image.paste(img, (0, y_offset))
            y_offset += img.size[1]

        self.current_picture = combined_image
    
    def save_picture(self):
        check = self.get_order_check()
        file_name = f"output/{check}_robot.jpg"
        self.current_picture.save(file_name)
    
    def make_all_orders(self):
        data = self.get_data_orders(BASE_URL)
        for data_item in data:
            self.close_modal_window()
            self.build_order(data_item)
            self.click_make_preview()
            self.make_picture(data_item)
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
        csv_file = []

        csv_url = "orders.csv"
        request_url = url + csv_url
        response = requests.get(url=request_url)
        csv_list = response.text.split("\n")
        csv_list.pop(0)

        for item in csv_list:
            new_list = item.split(",")[1:]
            csv_file.append(new_list)

        return csv_file

    def __del__(self):
        self.driver.quit()


my_robot = Robot()
my_robot.start()
