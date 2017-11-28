from abc import ABCMeta, abstractmethod


class LoginPageInterface(object, metaclass=ABCMeta):

    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def get_url(self):
        pass

    @abstractmethod
    def go_to_login_page(self):
        pass

    @abstractmethod
    def write_login(self):
        pass

    @abstractmethod
    def write_password(self):
        pass

    @abstractmethod
    def log_in_to_page(self):
        pass

    @abstractmethod
    def check_invalid(self):
        pass
