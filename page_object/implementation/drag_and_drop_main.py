from abc import ABCMeta
from page_object.interface.drag_and_drop_interface import DragAndDropInterface
from page_object.schema.drag_and_drop_schema import DragAndDropSchema


class DragAndDropMain(DragAndDropInterface, DragAndDropSchema, metaclass=ABCMeta):

    def get_url(self, url):
        self.driver.get(DragAndDropSchema.url)

