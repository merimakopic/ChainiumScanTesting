import unittest
import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Chrome()

class testingHome(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        browser.get("localhost:4200")
        browser.maximize_window
        time.sleep(4)
        browser.implicitly_wait(4)
    
    @classmethod
    def tearDownClass(self):
        browser.quit()

    def test_latestBlocks(self):
        table = browser.find_element_by_xpath('//*[@id="blockContainer"]/table')

        #check number of rows
        no_rows = len(table.find_elements_by_tag_name('tr')) - 2
        file = open("/home/merima/ChainiumScanTesting/Reports/Home/latest_blocks.txt", "w+")
        self.assertEqual(no_rows, 50, "Number of rows in latest blocks is not 50\n")
        file.write("Number of rows is 50. OK!\n")

        #check number of headers in table
        header_row = browser.find_element_by_xpath('//*[@id="blockContainer"]/table/thead/tr[2]')
        no_headers = len(header_row.find_elements_by_tag_name('th'))
        self.assertEqual(no_headers, 3, "Number of headers is not 3.\n")
        file.write("Number of column headers is 3. OK!\n")

        #check number of columns == number of cells in every row = 150
        no_col = len(table.find_elements_by_tag_name('td'))
        self.assertEqual(no_col, 50*3, "Number of columns is not 3\n")
        file.write("Number of columns is 3. OK!\n")

    def test_latestBlocks_data(self):
        table = browser.find_element_by_xpath('//*[@id="blockContainer"]/table')
            # get number of rows
        noOfRows = len(table.find_elements_by_xpath("//tr")) -2
            # get number of columns
        noOfColumns = len(table.find_elements_by_xpath('//tr[2]/td'))
        allData = []
            # iterate over the rows, to ignore the headers we have started the i with '1'
        for i in (2, noOfRows):
                # reset the row data every time
            ro = []
                # iterate over columns
            for j in (1, noOfColumns) :
                    # get text from the i th row and j th column
                wait = WebDriverWait(browser, 30)
                wait.until(EC.presence_of_element_located((By.XPATH, '//tr['+str(i)+']/td['+str(j)+']')))
                ro.append(table.find_element_by_xpath('//tr['+str(i)+']/td['+str(j)+']').text)
        
                # add the row data to allData of the self.table
            allData.append(ro)
        
        for i in range(0, len(allData)):
            print(allData[i])
            print()
            

if __name__ == '__main__':
    unittest.main()