import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

class testing(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        browser.get("localhost:4200")
        browser.implicitly_wait(5)
    @classmethod
    def tearDownClass(self):
        browser.quit()


    def test_linkNumber(self):
        links = browser.find_elements(By.TAG_NAME,"a")
        no_links = len(links)
        print("Number of links: ")
        print(no_links)
        print()
        for link in links:
            print(link.text)



if __name__ == '__main__':
    unittest.main()
