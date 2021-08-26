from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"C:\chromedriver_win32\chromedriver.exe")

driver.get("https://gmail.com")

usuario = driver.find_element_by_id("identifierId")
usuario.send_keys("iden.ticlla@gmail.com")
usuario.send_keys(Keys.ENTER)

time.sleep(3)

clave = driver.find_element_by_name("password")
clave.send_keys("123123")
clave.send_keys(Keys.ENTER)

time.sleep(3)

driver.close()
