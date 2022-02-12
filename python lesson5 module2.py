from selenium import webdriver
from math import *
import time

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_ele = browser.find_element_by_id("input_value")
    x = x_ele.text
    def calc(x):
        return str(log(abs(12*sin(int(x)))))
    y = calc(x)



    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()

    button_submit = browser.find_element_by_tag_name("button")
    button_submit.click()

finally:
    time.sleep(30)
    browser.quit()
