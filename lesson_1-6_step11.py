from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"
#link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block > .first_class > input")
    input1.send_keys('!!!   Имя тест')
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block > .second_class > input")
    input2.send_keys('!!!   Фамилия тест')
    input3 = browser.find_element(By.CSS_SELECTOR, '.first_block > .third_class > input')
    input3.send_keys('!!!   @почта тест')
    input4 = browser.find_element(By.CSS_SELECTOR, '.second_block > .first_class > input')
    input4.send_keys('!!!   +7 777 тест')
    input5 = browser.find_element(By.CSS_SELECTOR, '.second_block > .second_class > input')
    input5.send_keys('!!!   Адрес  тест')


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME,"h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
