from .base_page import BasePage
from locators import LoginLocators


class SigninPage(BasePage):

    def go_login(self):
        self.click_with_wait(LoginLocators.LOGIN_BUTTON)

    def go_logout(self):
        self.click_with_wait(LoginLocators.LOGOUT_BUTTON)

    def login(self, email, password):
        self.wait_for_overlay(LoginLocators.EMAIL)
        self.input_text(LoginLocators.EMAIL, email)
        self.input_text(LoginLocators.PASSWORD, password)
        self.click(LoginLocators.SUBMIT_BUTTON)

    def new_register(self):
        self.click_with_wait(LoginLocators.REGISTER_BUTTON)

    def check_elem(self):
        self.wait_for_overlay(LoginLocators.EMAIL)
        if not self.is_element_visible(LoginLocators.EMAIL):
            return False
        return True

    def check_elem_logout(self):
        self.wait_for_overlay(LoginLocators.LOGOUT_BUTTON)
        if not self.is_element_visible(LoginLocators.LOGOUT_BUTTON):
            return False
        else:
            return True