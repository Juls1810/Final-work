from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import keyboard
# data-tid

def test_search_by_name():
    # поиск фильма по названию на английском
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.kinopoisk.ru/")
    driver.implicitly_wait(20)
    driver.find_element(By.NAME, "kp_query").send_keys("Zootopia")
    keyboard.send("enter")
    driver.quit()


def test_aut_phone_number():
    # проверка валидного номера телефона(gпоз)
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.kinopoisk.ru/")
    sleep(15)
    driver.find_element(By.CLASS_NAME, 'styles_loginButton__6_QNl').click()
    driver.find_element(By.CLASS_NAME, 'Textinput-Control_phone-mask').send_keys("9046841027")
    driver.find_element(By.CSS_SELECTOR, '#passp:sign-in').click()
    driver.quit()

def test_aut_phone_number_neg():
    # проверка не валидного номера телефона(нег)
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.kinopoisk.ru/")
    sleep(15)
    driver.find_element(By.CLASS_NAME, 'styles_loginButton__6_QNl').click()
    driver.find_element(By.CLASS_NAME, 'Textinput-Control_phone-mask').send_keys("904")
    driver.find_element(By.CLASS_NAME, 'Button2_width_max Button2_type_submit').click()
    driver.quit()

def test_search_by_actor_name():
    # поиск актера
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.kinopoisk.ru/")
    driver.implicitly_wait(20)
    driver.find_element(By.NAME, "kp_query").send_keys("Петров")
    sleep(12)
    keyboard.send("enter")
    driver.quit()

def test_search_by_genre():
    # поиск жанра
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.kinopoisk.ru/")
    driver.implicitly_wait(20)
    driver.find_element(By.NAME, "kp_query").send_keys("Анимэ")
    keyboard.send("enter")
    driver.quit()


