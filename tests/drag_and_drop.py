import unittest
from selenium import webdriver
from page_object.implementation.drag_and_drop_main import DragAndDropMain
from page_object.schema.drag_and_drop_schema import DragAndDropSchema


class DragAndDrop(unittest.TestCase, DragAndDropSchema):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://www.google.com/")

    def test_url(self):
        #obiekt = DragAndDrop(self.driver)

        DragAndDropSchema.get_url()
        #self.driver.get("http://demo.magentocommerce.com")


if __name__ == '__main__':
    unittest.main()
