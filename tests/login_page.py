import unittest
from page_object.interface.base_test_case import BaseTestCase
from page_object.implementation.login_page_main import LoginPageMain


class LoginPage(BaseTestCase):

    def test_login_page(self):
        obi = LoginPageMain(self.driver)
        obi.get_url()
        obi.go_to_login_page()
        obi.write_login()
        obi.write_password()
        obi.log_in_to_page()
        obi.check_invalid()


if __name__ == "__main__":
    unittest.main(verbosity=2)