import os
import pytest
from app.yandex_auth import YandexAuth
from selenium import webdriver


@pytest.fixture(scope='class')
def data():
    browser = webdriver.Chrome()
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    link = 'https://passport.yandex.ru/auth/'
    correct_auth = YandexAuth(login, password, browser, link)
    invalid_login = YandexAuth('invalidlogin@yru', password, browser, link)
    invalid_password = YandexAuth(login, 'qwerty', browser, link)
    return correct_auth, invalid_login, invalid_password


class TestYandexAuth:

    def test_auth_correct(self, data):
        result = data[0].authorize()
        assert result is True

    def test_auth_invalid_login(self, data):
        result = data[1].authorize()
        assert result == 'Invalid login'

    def test_auth_invalid_password(self, data):
        result = data[2].authorize()
        assert result == 'Invalid password'
