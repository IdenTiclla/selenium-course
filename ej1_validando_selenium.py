from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"C:\chromedriver_win32\chromedriver.exe")
driver.get("https://google.com.bo")
driver.close()
