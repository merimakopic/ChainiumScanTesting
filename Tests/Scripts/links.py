import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

class testing(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        browser.get("localhost:4200")
        browser.implicitly_wait(10)
    @classmethod
    def tearDownClass(self):
        browser.quit()

    def test_linkNumber(self):
        links = browser.find_elements(By.TAG_NAME,"a")
        no_links = len(links)
        file = open("/home/merima/ChainiumScanTesting/Reports/linkNumber.txt","w+")
        file.write("Number of links: %d \n" %no_links)
        file.write("Existing texts of links: \n")
        text_no = 0
        for link in links:
            if link.text != "":
                text_no = text_no + 1
            file.write(link.text)
            file.write("\n")
        
        #need to check how many links have texts
        if text_no == no_links:
            file.write("All links have texts")
        else:
            file.write("NUMBER OF LINKS THAT DOES NOT HAVE TEXT: %d" %(no_links-text_no))
        file.close()



if __name__ == '__main__':
    unittest.main()
