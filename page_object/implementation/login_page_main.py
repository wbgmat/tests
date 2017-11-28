import unittest
from abc import ABCMeta
from page_object.interface.login_page_interface import LoginPageInterface
from page_object.schema.login_page_schema import LoginPageSchema


class LoginPageMain(LoginPageInterface, LoginPageSchema, unittest.TestCase, metaclass=ABCMeta):

    def __init__(self, driver):
        super(LoginPageMain, self).__init__(driver)

    def get_url(self):
        self.driver.get(self._url)

    def go_to_login_page(self):
        my_account = self.driver.find_element_by_xpath(self._my_account)
        my_account.click()
        login = self.driver.find_element_by_xpath(self._login)
        login.click()

    def write_login(self):
        email = self.driver.find_element_by_name(self._email_field)
        email.send_keys(self._email)

    def write_password(self):
        password = self.driver.find_element_by_name(self._password_field)
        password.send_keys(self._password)

    def log_in_to_page(self):
        log_in = self.driver.find_element_by_xpath(self._log_in)
        log_in.click()

    def check_invalid(self):
        invalid = self.driver.find_element_by_xpath(self._invalid)
        self.assertTrue(invalid.is_displayed())