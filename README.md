# Final-work. Автоматизация тестирования 
# pytest_ui_api_template

## Данные тесты предназначены для тестирования API и UI сервиса Кинопоиск
Онлайн-сервис Кинопоиск для просмотра фильмов, сериалов, ТВ Каналов и покупки билетов в кино
Сервис предоставляет возможность поиска фильма, получение информации о фильме (краткое содержание, рейтинг, год выхода, страна, актеры, режиссёр)просмотра трейлера, выставления оценки после просмотра, написания рецензии
В данном сервисе доступно более 100 телеканалов разделенных по категориям.
В сервисе присутствует возможность приобрести билет в кинотеатр.

Для запуска API тестов используется команда  pytest test_API.py
Для запуска UI тестов используется команда pytest Test_Ui
Для запуска всех тестов используется команда pytest 
Для формирования отчета используется команда pytest --alluredir allure-result 
Для запуска Allure и конвертирования результата теста в отчет allure serve allure-result

### Стек:
- pytest
- keyboard
- selenium
- requests
- _sqlalchemy_from selenium.webdriver.common.by import By
- sqlalchemy_from selenium.webdriver.common.by import Keys
- sqlalchemy_from selenium.webdriver.common.by import WebDriverWait
- sqlalchemy_from selenium.webdriver.common.by import as EC


