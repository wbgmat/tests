import unittest
from selenium import webdriver
from page_object.interface.base_test_case import BaseTestCase
from page_object.implementation.drag_and_drop_main import DragAndDropMain
from page_object.schema.drag_and_drop_schema import DragAndDropSchema
from selenium.webdriver.common.action_chains import ActionChains


class DragAndDrop(BaseTestCase, DragAndDropMain):

    def test_drag_and_dropdrop(self):
        obi = DragAndDropMain(self.driver)
        obi.get_url()
        obi.drag_drop()


if __name__ == "__main__":
    unittest.main(verbosity=2)

