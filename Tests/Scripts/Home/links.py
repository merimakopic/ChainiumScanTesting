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
        file = open("/home/merima/ChainiumScanTesting/Reports/Home/linkNumber.txt","w+")
        file.write("Number of links: %d \n\n" %no_links)
        file.write("Existing texts of links: \n")
        text_no = 0
        address = ""
        for link in links:
            if link.text != "":
                text_no = text_no + 1
            address = link.get_attribute("href")
            file.write(link.text)
            file.write(" = ")
            file.write(address)
            file.write("\n")
        #need to check how many links have texts
        if text_no == no_links:
            file.write("\n All links have texts \n")
        else:
            file.write("\n NUMBER OF LINKS THAT DOES NOT HAVE TEXT: %d \n" %(no_links-text_no))
        file.close()



if __name__ == '__main__':
    unittest.main()
