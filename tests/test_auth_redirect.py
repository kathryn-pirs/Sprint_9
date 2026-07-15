import allure
from data.data import URLs


@allure.title("Редирект неавторизованных пользователей")
class TestAuthRedirect:

    @allure.story("Проверка редиректа со страницы создания рецепта")
    def test_create_recipe_redirects_to_login(self, browser):
        with allure.step("Попытаться открыть страницу создания рецепта"):
            browser.get(URLs.CREATE_URL)

        with allure.step("Проверить, что произошёл редирект на страницу входа"):
            assert browser.current_url == URLs.LOGIN_URL, \
                f"Не выполнен редирект на страницу входа: {browser.current_url}"

    @allure.story("Проверка редиректа с главной страницы")
    def test_main_page_redirects_to_login(self, browser):
        with allure.step("Открыть главную страницу"):
            browser.get(URLs.BASE_URL)

        with allure.step("Проверить, что произошёл редирект на страницу входа"):
            assert browser.current_url == URLs.LOGIN_URL, \
                f"Не выполнен редирект на страницу входа: {browser.current_url}"

    @allure.story("Проверка редиректа со страницы подписок")
    def test_subscriptions_redirects_to_login(self, browser):
        with allure.step("Попытаться открыть страницу подписок"):
            browser.get(URLs.SUB_URL)

        with allure.step("Проверить, что произошёл редирект на страницу входа"):
            assert browser.current_url == URLs.LOGIN_URL, \
                f"Не выполнен редирект на страницу входа: {browser.current_url}"
