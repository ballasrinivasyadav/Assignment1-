import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome("C:\\Users\\Srinivas\\PycharmProjects\\Assignment1\\Driver\\chromedriver.exe")
driver.get("https://www.amazon.in/")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys("iphone xr 64gb yellow")
time.sleep(2)

driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()
time.sleep(4)
price1 = driver.find_element(By.XPATH,"//span[normalize-space()='47,999']").text
print(price1)
time.sleep(5)

driver.get("https://www.flipkart.com/")

driver.find_element(By.XPATH,"//input[@class='_3704LK']").send_keys("iphone")
time.sleep(5)
driver.find_element(By.XPATH,"//button[@type='submit']//*[name()='svg']").click()
time.sleep(10)
driver.find_element(By.XPATH,"//div[normalize-space()='APPLE iPhone 11 (White, 64 GB)']").click()

price2 = driver.find_element(By.XPATH,"//body/div[@id='container']/div/div[@class='_36fx1h _6t1WkM _3HqJxg']/div[@class='_1YokD2 _2GoDe3']/div[@class='_1YokD2 _3Mn1Gg']/div[2]/div[1]/div[1]/div[1]/a[1]/div[2]/div[2]/div[1]/div[1]/div[1]").text
print(price2)
if price1 < price2:
    print("Buy from Amazon")
else:
    print("Buy from Flipkart")

