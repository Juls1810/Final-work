import requests
import pytest

base_url = "https://api.kinopoisk.dev/"
headers = {
        'X-API-KEY': 'VPCDTQ7-47B44DY-QBGZ77D-YM7HV9D',
        'Content-Type': 'application/json'
    }

def test_kp_search_by_id():
    resp = requests.get(url=base_url + '/v1.4/movie/666', headers=headers)
    assert resp.status_code == 200
    assert resp.json()["id"] == 666
    assert resp.json()["name"] == "Форсаж"

def test_kp_search_by_name():
    resp = requests.get(url=base_url + '/v1.4/movie/search?page=1&limit=10&query=zootopia', headers=headers)
    assert resp.status_code == 200
    assert resp.json().get("docs", [{}])[0].get("id") == 775276
    assert resp.json().get("docs", [{}])[0].get("name") == "Зверополис"


def test_kp_search_seasons():
    resp = requests.get(url=base_url + '/v1.4/season?notNullFields=enName&movieId=571335&number=10', headers=headers)
    assert resp.status_code == 200
    assert resp.json().get("docs", [{}])[0].get("movieId") == 571335
    assert resp.json().get("docs", [{}])[0].get("number") == 10


def test_kp_search_by_id_post():
    resp = requests.post(url=base_url + '/v1.4/movie/666', headers=headers)
    assert resp.status_code == 404


def test_kp_search_by_id_delete():
    resp = requests.delete(url=base_url + '/v1.4/movie/666', headers=headers)
    assert resp.status_code == 404

