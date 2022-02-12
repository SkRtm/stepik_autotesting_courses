from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import *


link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link)

price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

button_book = browser.find_element(By.ID, "book").click()

value = browser.find_element(By.ID, "input_value")
x = value.text

def calc(x):
    return str(log(abs(12*sin(int(x)))))

y = calc(x)

input_answer = browser.find_element(By.ID, "answer").send_keys(y)

button_submit = browser.find_element(By.ID, "solve").click()

print(browser.switch_to.alert.text)
browser.quit()