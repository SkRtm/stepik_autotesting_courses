#from math import *
#x = str(ceil(pow(pi, e)*10000))
#print(x)

from selenium import webdriver
import time

link_site = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link_site)

    link = browser.find_element_by_link_text("224592")
    link.click()

    input1 = browser.find_element_by_css_selector("form > div:nth-child(1) > input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(30)
    browser.quit()
