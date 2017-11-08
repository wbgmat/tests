from abc import ABCMeta, abstractmethod


class DragAndDropInterface(object, metaclass=ABCMeta):

    @abstractmethod
    def dragdrop(self, source, target):
        pass

    @abstractmethod
    def get_url(self):
        pass

