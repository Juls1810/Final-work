fimport allure
import pytest
from selenium import webdriver
from SearchPageKP import SearchPageKP
from LoginPageKP import LoginPageKP

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.kinopoisk.ru/")
    driver.implicitly_wait(20)
    yield driver
    driver.quit()


def test_kp():
    log_page = LoginPageKP(driver)
    log_page.test_aut_phone_number()
    log_page.test_aut_phone_number_neg()

    cearch_page = SearchPageKP(driver)
    cearch_page.test_search_by_name()
    cearch_page.test_search_by_actor_name()
    cearch_page.test_search_by_genre()