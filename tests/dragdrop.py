from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

class DragDrop(object):

    def __init__(self, driver):
        self.driver = driver

    def abc(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("https://the-internet.herokuapp.com/drag_and_drop")
        source = self.driver.find_element_by_id("column-a")
        target = self.driver.find_element_by_id("column-b")
        abc = ActionChains(self.driver).drag_and_drop(self.source, self.target)
        abc.perform()

    abc1 = DragDrop()
    abc1.abc()