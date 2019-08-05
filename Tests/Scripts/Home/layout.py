import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

browser = webdriver.Chrome()

class testingHome(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        options = Options()
        options.add_argument("--kiosk")
        browser.get("localhost:4200")
        browser.implicitly_wait(3)
        time.sleep(4)
    @classmethod
    def tearDownClass(self):
        browser.quit()

    def test_screenshot(self):
        browser.save_screenshot("/home/merima/ChainiumScanTesting/Reports/Home/layout.png")


if __name__ == "__main__":
    unittest.main()
