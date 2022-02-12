from tkinter import Y
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1") #Ищет х
    num2 = browser.find_element_by_id("num2") #Ищет y
    x = int(num1.text) #Перевод 
    y = int(num2.text)
    result = str(x + y)

    dropdown = Select(browser.find_element_by_id("dropdown"))
    dropdown.select_by_value(result)

    button_submit = browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(10)
    browser.quit()