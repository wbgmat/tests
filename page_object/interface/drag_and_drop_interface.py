from abc import ABCMeta, abstractmethod


class DragAndDropInterface(object, metaclass=ABCMeta):

    def __init__(self, driver):
        self.driver = driver

    @abstractmethod
    def drag_drop(self, source, target):
        pass

    @abstractmethod
    def get_url(self):
        pass

