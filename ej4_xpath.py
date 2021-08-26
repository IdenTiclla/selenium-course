import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# 2 tipos de xpath: relativo, absoluto
# relativo

#absoluto

# xpath es una estructura de objetos.
class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\chromedriver_win32\chromedriver.exe")

    def test_buscar_por_xpath(self):
        driver = self.driver
        driver.get("http://google.com")
        time.sleep(3)
        buscar_por_xpath = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        time.sleep(3)
        buscar_por_xpath.send_keys("selenium", Keys.ARROW_DOWN)
        time.sleep(3)
        
    def tearDown(self):
        return self.driver.close()

if __name__ == "__main__":
    unittest.main()
