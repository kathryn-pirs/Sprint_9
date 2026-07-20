import allure
from pages.signin_page import SigninPage
from data.data import URLs


@allure.story("Авторизация")
class TestSignin:

    @allure.title("Проверка отображения формы входа")
    def test_signin_form_displayed(self, browser):
        signin = SigninPage(browser)

        with allure.step("Открыть страницу входа"):
            signin.open(URLs.LOGIN_URL)

        with allure.step("Проверить отображение формы входа"):
            assert signin.check_elem(), "Форма входа не отображается"

        with allure.step("Проверить URL страницы входа"):
            assert signin.get_current_url() == URLs.LOGIN_URL, \
                f"Открыт неверный URL: {signin.get_current_url()}"

    @allure.title("Проверка авторизации: переход на главную и кнопка «Выход»")
    def test_authorization_redirect_and_logout(self, browser, authorized_user):
        login = SigninPage(browser)

        with allure.step("Проверить переход на главную страницу"):
            login.wait_for_url_change(URLs.RECIPES_URL)
            assert login.get_current_url() == URLs.RECIPES_URL, \
                f"Открыт неверный URL: {login.get_current_url()}"

        with allure.step("Проверить отображение кнопки «Выход»"):
            login.open(URLs.BASE_URL)
            assert login.check_elem_logout(), "Кнопка выхода не отображается"
