import unittest
from time import sleep
from selenium import webdriver


class TestThree(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.driver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities={
                "browserName": "chrome",
            })
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test_three(self):
        self.driver = self.driver
        self.driver.get("https://www.twitter.com")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()