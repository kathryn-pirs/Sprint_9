import allure
from conftest import BACKEND_AUTH_AVAILABLE
from pages.signin_page import SigninPage
from data.data import URLs


@allure.title("Авторизация")
class TestSignin:

    @allure.story("Проверка отображения формы входа")
    def test_signin_form_displayed(self, browser):
        signin = SigninPage(browser)

        with allure.step("Открыть страницу входа"):
            signin.open(URLs.LOGIN_URL)

        with allure.step("Проверить отображение формы входа"):
            assert signin.check_elem(), "Форма входа не отображается"

        with allure.step("Проверить URL страницы входа"):
            assert browser.current_url == URLs.LOGIN_URL, \
                f"Открыт неверный URL: {browser.current_url}"

    @allure.story("Проверка авторизации: переход на главную и кнопка «Выход»")
    def test_authorization_redirect_and_logout(self, browser, authorized_user):
        login = SigninPage(browser)

        with allure.step("Проверить переход на главную страницу"):
            login.wait_for_url_change(URLs.RECIPES_URL)
            assert browser.current_url == URLs.RECIPES_URL, \
                f"Открыт неверный URL: {browser.current_url}"

        with allure.step("Проверить отображение кнопки «Выход»"):
            login.open(URLs.BASE_URL)
            assert login.check_elem_logout(), "Кнопка выхода не отображается"
