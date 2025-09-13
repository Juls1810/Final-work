from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import keyboard
import pytest

class SearchPageKP:"""
                   Конструктор класса SearchPageKP
    """
    def __init__(self, driver):
        self._driver = driver

    def search_by_name(self):
        self._driver.find_element(By.NAME, "kp_query").send_keys("Zootopia")
        keyboard.send("enter")
        push_window = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "name")))
        assert "Зверополис" in push_window.text

    def search_by_actor_name(self):
        self._driver.find_element(By.NAME, "kp_query").send_keys("Петров")
        keyboard.send("enter")
        push_window = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "name")))
        assert "Александр Петров" in push_window.text

    def search_by_genre(self):
        self._driver.find_element(By.NAME, "kp_query").send_keys("Анимэ")
        keyboard.send("enter")
        push_window = WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "name")))
        assert "Аниме" in push_window.text

