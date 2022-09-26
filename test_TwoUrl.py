import time
from selenium import webdriver
from selenium.webdriver.common.by import By

first_page = "https://www.amazon.in/"
second_page = "https://www.flipkart.com/"

driver = webdriver.Chrome("C:\\Users\\Srinivas\\PycharmProjects\\Assignment1\\Driver\\chromedriver.exe")
driver.get(first_page)
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys("iphone xr 64gb yellow")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()
time.sleep(5)
price1 = driver.find_element(By.XPATH,"//span[normalize-space()='99,900']").text
print(price1)
time.sleep(5)

driver.execute_script("window.open('" + second_page + "')")

