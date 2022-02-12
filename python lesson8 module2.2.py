from distutils.command.upload import upload
from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    input_name = browser.find_element_by_css_selector('input[placeholder="Enter first name"]')
    input_name.send_keys("Ivan")

    input_last_name = browser.find_element_by_css_selector('input[placeholder="Enter last name"]')
    input_last_name.send_keys("Ivanov")

    input_email = browser.find_element_by_css_selector('input[placeholder="Enter email"]')
    input_email.send_keys("Ivan@mail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "test_file_for_lesson8_module2.2.txt")

    upload_button = browser.find_element_by_id("file")
    upload_button.send_keys(file_path)

    button_submit = browser.find_element_by_tag_name('button').click()

finally:
    time.sleep(20)
    browser.quit()