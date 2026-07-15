from .base_page import BasePage
from locators import SignupLocators


class SignupPage(BasePage):
    def register(self, name, lastname, username, email, password):
        self.wait_for_overlay(SignupLocators.FIRST_NAME)
        self.input_text(SignupLocators.FIRST_NAME, name)
        self.input_text(SignupLocators.LAST_NAME, lastname)
        self.input_text(SignupLocators.USERNAME, username)
        self.input_text(SignupLocators.EMAIL, email)
        self.input_text(SignupLocators.PASSWORD, password)
        self.click(SignupLocators.SUBMIT)

    def check_elem(self):
        self.wait_for_overlay(SignupLocators.EMAIL)
        if not self.is_element_visible(SignupLocators.EMAIL):
            return False
        else:
            return True

    def go_logout(self):
        self.click_with_wait(SignupLocators.LOGOUT_BUTTON)