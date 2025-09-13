import requests
import pytest
import allure

base_url = "https://api.kinopoisk.dev/"
headers = {
        'X-API-KEY': 'VPCDTQ7-47B44DY-QBGZ77D-YM7HV9D',
        'Content-Type': 'application/json'
    }


@allure.title("API тестирование сервиса Кинопоиск")
@allure.description("Тестs проверяют возможность авторизации на портале с валидным и невалидным номером телефона,"
                    " а так же поиск фильмов,жанров и актеров")
@allure.feature("Сервис Кинопоиск")
@allure.severity(allure.severity_level.CRITICAL)

def test_kp_search_by_id():
    """
        Тест проверяет поиск фильма по id
    """
    resp = requests.get(url=base_url + '/v1.4/movie/666', headers=headers)
    assert resp.status_code == 200
    assert resp.json()["id"] == 666
    assert resp.json()["name"] == "Форсаж"


def test_kp_search_by_name():
    """
            Тест проверяет поиск фильма по названию
        """
    resp = requests.get(url=base_url + '/v1.4/movie/search?page=1&limit=10&query=zootopia', headers=headers)
    assert resp.status_code == 200
    assert resp.json().get("docs", [{}])[0].get("id") == 775276
    assert resp.json().get("docs", [{}])[0].get("name") == "Зверополис"


def test_kp_search_seasons():
    """
            Тест проверяет поиск сезона сериала
        """
    resp = requests.get(url=base_url + '/v1.4/season?notNullFields=enName&movieId=571335&number=10', headers=headers)
    assert resp.status_code == 200
    assert resp.json().get("docs", [{}])[0].get("movieId") == 571335
    assert resp.json().get("docs", [{}])[0].get("number") == 10


def test_kp_search_by_id_post():
    """
            Тест проверяет поиск методом post
    """
    resp = requests.post(url=base_url + '/v1.4/movie/666', headers=headers)
    assert resp.status_code == 404


def test_kp_search_by_id_delete():
    """
            Тест проверяет возможность использования метода delite
        """
    resp = requests.delete(url=base_url + '/v1.4/movie/666', headers=headers)
    assert resp.status_code == 404

