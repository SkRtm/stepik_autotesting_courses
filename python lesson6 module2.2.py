from selenium import webdriver
import time
from math import *

link = "http://suninjuly.github.io/execute_script.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    x_ele = browser.find_element_by_id("input_value")
    x = x_ele.text

    def calc(x):
        return str(log(abs(12*sin(int(x)))))

    y = calc(x)

    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    checkbox = browser.find_element_by_id("robotCheckbox").click()

    radiobutton = browser.find_element_by_id("robotsRule").click()

    button.click()

finally:
    time.sleep(20)
    browser.quit()
