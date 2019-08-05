import unittest
from time import sleep
from selenium import webself.driver


class TestThree(unittest.TestCase):
    def setUp():
        self.driver = webself.driver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities={
                "browserName": "chrome",
            })
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test_three():
        self.driver = self.driver
        self.driver.get("https://www.twitter.com")

    def tearDown():
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()