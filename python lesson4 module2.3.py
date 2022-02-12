from selenium import webdriver
import time
from math import *

link = "http://suninjuly.github.io/alert_accept.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    button_journey = browser.find_element_by_tag_name("button").click()

    confirm = browser.switch_to.alert.accept()

    value = browser.find_element_by_id("input_value")

    x = value.text
    def calc(x):
        return str(log(abs(12*sin(int(x)))))
    y = calc(x)
    
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    button_submit = browser.find_element_by_tag_name("button").click()

finally:
    print(browser.switch_to.alert.text)
    browser.quit()


