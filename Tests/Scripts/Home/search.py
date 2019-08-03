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
        wait.until(EC.visibility_of_element_located((By.ID, "UserInput")))
        search = browser.find_element_by_id("UserInput")
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
        search.clear()
        curr_url = browser.current_url
        search.send_keys("something", Keys.ENTER)
        new_url = browser.current_url
        if curr_url == new_url:
            file.write("ENTER KEY ON SEARCH ELEMENT DOES NOT WORK. INPUT ELEMENT WITH ID = UserInput\n")
        else:
            file.write("ENTER key on search element works\n")

        #check whether, warning about invalid input exists in search algorithm
        #search can be done by block / transaction / address / account / asset / validator
        #it opens the same template of a page with different information, when search text is valid
        #what happens if search text is not valid?
        search.clear()
        search.send_keys("13169")
        search_button = browser.find_element_by_xpath('//*[@id="Search-Bar"]/div/div/div/div/button')
        search_button.click()
        html = browser.page_source
        if "Basic Info" and "Additional Info" in html:
            file.write("Search opens right page\n")
        else:
            file.write("SEARCH DOES NOT OPEN RIGHT PAGE. SEARCH BY BLOCK NUMBER: 13169\n")

        browser.back()
        search = browser.find_element_by_id("UserInput")
        search.click()
        search.clear()
        search.send_keys("invalidinvalidinvalidinvalid")
        search_button = browser.find_element_by_xpath('//*[@id="Search-Bar"]/div/div/div/div/button')
        search_button.click()
        if "Basic Info" and "Additional Info" in html:
            file.write("INFORMATION ABOUT 'No result for searched page, or invalid input' - THAT SHOULD BE ADDED\n")

        file.write("\nThis is not testing of search algorithm, just of search bar element!\n")        


if __name__ == "__main__":
    unittest.main()