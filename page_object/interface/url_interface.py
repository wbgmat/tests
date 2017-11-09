from abc import ABCMeta, abstractmethod


class UrlInterface(object, metaclass=ABCMeta):
    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def get_url(self):
        pass
