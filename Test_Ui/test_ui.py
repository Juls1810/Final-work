import allure
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

@allure.title("UA тестирование сервиса Кинопоиск")
@allure.description("Тесты проверяют возможность авторизации на портале с валидным и невалидным номером телефона,"
                    " а так же поиск фильмов,жанров и актеров")
@allure.feature("Сервис Кинопоиск")
@allure.severity(allure.severity_level.CRITICAL)
def test_ui(driver):
    with allure.step("Обьявляем переменную"):
    log_page = LoginPageKP(driver)
    """
            Тест проверяет позможность авторизации с валидным номером
    """
    log_page.aut_phone_number()
    """
        Тест проверяет позможность авторизации с не валидным номером
    """
    log_page.aut_phone_number_neg()

    with allure.step("Обьявляем переменную"):
    cearch_page = SearchPageKP(driver)
    """
            Тест проверяет позможность поиска по названию фильма
    """
    cearch_page.search_by_name()
    """
               Тест проверяет позможность поиска по имени актера
       """
    cearch_page.search_by_actor_name()
    """
               Тест проверяет позможность поиска по жанру
       """
    cearch_page.search_by_genre()