import allure
from pages.signin_page import SigninPage
from data.data import URLs


@allure.title("Редирект неавторизованных пользователей")
class TestAuthRedirect:

    @allure.story("Проверка редиректа со страницы создания рецепта")
    def test_create_recipe_redirects_to_login(self, browser):
        signin = SigninPage(browser)

        with allure.step("Попытаться открыть страницу создания рецепта"):
            signin.open(URLs.CREATE_URL)

        with allure.step("Проверить, что произошёл редирект на страницу входа"):
            assert signin.get_current_url() == URLs.LOGIN_URL, \
                f"Не выполнен редирект на страницу входа: {signin.get_current_url()}"

    @allure.story("Проверка редиректа с главной страницы")
    def test_main_page_redirects_to_login(self, browser):
        signin = SigninPage(browser)

        with allure.step("Открыть главную страницу"):
            signin.open(URLs.BASE_URL)

        with allure.step("Проверить, что произошёл редирект на страницу входа"):
            assert signin.get_current_url() == URLs.LOGIN_URL, \
                f"Не выполнен редирект на страницу входа: {signin.get_current_url()}"

    @allure.story("Проверка редиректа со страницы подписок")
    def test_subscriptions_redirects_to_login(self, browser):
        signin = SigninPage(browser)

        with allure.step("Попытаться открыть страницу подписок"):
            signin.open(URLs.SUB_URL)

        with allure.step("Проверить, что произошёл редирект на страницу входа"):
            assert signin.get_current_url() == URLs.LOGIN_URL, \
                f"Не выполнен редирект на страницу входа: {signin.get_current_url()}"
