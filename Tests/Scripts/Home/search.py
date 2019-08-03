import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

browser = webdriver.Chrome()

class testing(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        browser.get("localhost:4200")
        browser.implicitly_wait(3)
    @classmethod
    def tearDownClass(self):
        browser.quit()

    def test_search(self):
        wait = WebDriverWait(browser, 3)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Search-Bar"]/div/div')))
        search = browser.find_element_by_css_selector("#Search-Bar > div > div > div")
        file = open("/home/merima/ChainiumScanTesting/Reports/Home/search.txt", "w+")
        file.write("Search element is located\n")
        if search.is_displayed():
            file.write("Search element is displayed\n")
        else:
            file.write("SEARCH ELEMENT IS NOT DISPLAYED\n")
        if search.is_enabled():
            file.write("Search element is enabled\n")
        else:
            file.write("SEARCH ELEMENT IS NOT ENABLED\n")
        search.click()
        search.clear

        search.send_keys("something")
       

if __name__ == "__main__":
    unittest.main()