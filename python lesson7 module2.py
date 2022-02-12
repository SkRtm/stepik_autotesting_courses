from selenium import webdriver
from math import *
import time

link = "http://suninjuly.github.io/get_attribute.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element_by_id("treasure")
    x_ele = treasure.get_attribute("valuex")
    x = x_ele
    def calc(x):
        return str(log(abs(12*sin(int(x)))))
    y = calc(x)

    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    check_box = browser.find_element_by_id("robotCheckbox").click()

    radio_b = browser.find_element_by_id("robotsRule").click()

    button_submit = browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(10)
    browser.quit()