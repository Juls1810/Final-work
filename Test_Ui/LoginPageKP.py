from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard
import pytest


class LoginhPageKP:
    """
           Конструктор класса LoginhPageKP
    """
    def __init__(self, driver):
        self._driver = driver

    def aut_phone_number(self):
        self._driver.find_element(By.CLASS_NAME, 'styles_loginButton__6_QNl').click()
        self._driver.find_element(By.CLASS_NAME, 'Textinput-Control_phone-mask').send_keys("9046841027")
        keyboard.send("enter")
        push_window = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "TitleWithDeviceList")))
        assert "Введите код из пуш-уведомления " in push_window.text

    def aut_phone_number_neg(self):
        self._driver.find_element(By.CLASS_NAME, 'styles_loginButton__6_QNl').click()
        self._driver.find_element(By.CLASS_NAME, 'Textinput-Control_phone-mask').send_keys("904")
        keyboard.send("enter")
        push_window = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "Textinput-Hint")))
        assert "Недопустимый формат номера" in push_window.text
