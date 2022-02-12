from selenium import webdriver
from math import *

def calc(x):
    return str(log(abs(12*sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()
browser.get(link)

button_redirect = browser.find_element_by_class_name("trollface.btn").click()

browser.switch_to.window(browser.window_handles[1])

value = browser.find_element_by_id("input_value")
x = value.text
y = calc(x)

input_answer = browser.find_element_by_id("answer")
input_answer.send_keys(y)

button_submit = browser.find_element_by_css_selector('button[type="submit"]').click()

print(browser.switch_to.alert.text)
browser.quit()