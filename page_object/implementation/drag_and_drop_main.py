from abc import ABCMeta
from page_object.interface.drag_and_drop_interface import DragAndDropInterface
from page_object.schema.drag_and_drop_schema import DragAndDropSchema
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


class DragAndDropMain(DragAndDropInterface, DragAndDropSchema, ActionChains, metaclass=ABCMeta):

    def __init__(self, driver):
        super(DragAndDropMain, self).__init__(driver)
        # self.source = source
        # self.target = target

    def get_url(self):
        self.driver.get(self._url)

    def drag_drop(self):
        # driver = self.driver
        source = self.driver.find_element_by_id(self._source)
        target = self.driver.find_element_by_id(self._target)
        ActionChains(self.driver).drag_and_drop(source, target).perform()





