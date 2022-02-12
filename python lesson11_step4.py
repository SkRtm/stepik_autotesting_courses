from selenium import webdriver
import time

#Ссылка на первую форму регистрации
#link = "http://suninjuly.github.io/registration1.html" 

#Ссылка на вторую форму регистрации
link2 = "http://suninjuly.github.io/registration2.html" 



try:

    browser = webdriver.Chrome()
    browser.get(link2)

    input1 = browser.find_element_by_css_selector('input[placeholder="Input your first name"]') #Поиск и заполнение первого обязательного поля
    input1.send_keys("Иван")

    input2 = browser.find_element_by_css_selector('input[placeholder="Input your last name"]') #Поиск и заполнение второго обязательного поля
    input2.send_keys("Иванов")

    input3 = browser.find_element_by_css_selector('input[placeholder="Input your email"]') #Поиск и заполнение третьего обязательного поля
    input3.send_keys("test@mail.com")

    button = browser.find_element_by_css_selector('button[type="Submit"]')
    button.click()

    time.sleep(5)

    welcome_text = browser.find_element_by_css_selector("div.container > h1").text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:

    time.sleep(10)
    browser.quit()