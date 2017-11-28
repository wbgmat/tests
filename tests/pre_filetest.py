import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


class FileTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def test_search(self):
        # self.driver.get("http://www.phptravels.net/")
        pass

    def test_preparation(self):
        self.driver.get("http://www.phptravels.net/")
        my_account = self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/ul/ul/li[1]/a')
        my_account.click()
        login = self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/ul/ul/li[1]/ul/li[1]/a')
        login.click()
        email = self.driver.find_element_by_name('username')
        email_check = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/form/div[1]/div[5]/div/div[1]/label')
        self.assertTrue(email_check.is_displayed())
        email.send_keys("wbgmat@gmail.com")
        password = self.driver.find_element_by_name('password')
        password.send_keys("abcabc111")
        log_in = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/form/div[1]/div[5]/button')
        log_in.click()
        invalid = self.driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/form/div[1]/div[2]/div')
        # assert not invalid.is_displayed()
        self.assertTrue(invalid.is_displayed())
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
