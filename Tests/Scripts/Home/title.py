import unittest
from selenium import webdriver

browser = webdriver.Chrome()

class testingHome(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        browser.get("localhost:4200")
        browser.implicitly_wait(3)
    @classmethod
    def tearDownClass(self):
        browser.quit()

    def test_title(self):
        title = browser.title
        exp_title = "ChainiumScan"
        file = open("/home/merima/ChainiumScanTesting/Reports/Home/title.txt", "w+")
        file.write("Title of page: %s\n" %title)
        self.assertEqual(title, exp_title)
        file.write("Title is OK\n")
        
if __name__ == "__main__":
    unittest.main()