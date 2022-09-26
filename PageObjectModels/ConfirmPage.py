import time
from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    amZconfirm = (By.XPATH, "//input[@id='nav-search-submit-button']")
    amZprice = (By.XPATH, "//span[normalize-space()='1,00,900']")
    flipKconfirm = (By.XPATH, "//button[@type='submit']//*[name()='svg']")
    flipenter = (By.XPATH, "//div[normalize-space()='APPLE iPhone 13 (Green, 128 GB)']")
    click = (By.XPATH, "//div[@class='_30jeq3 _16Jk6d']")

    def getconfirmpage(self):
        self.driver.find_element(*CheckOutPage.amZconfirm).click()

    def getclickrpage(self):
        return self.driver.find_element(*CheckOutPage.amZprice).text

    def getflipconfirmpage(self):
        self.driver.find_element(*CheckOutPage.flipKconfirm).click()
        time.sleep(10)

    def getflipkartenter(self):
        return self.driver.find_element(*CheckOutPage.flipenter).text

    def getclickflipkart(self):
        self.driver.find_element(*CheckOutPage.click)
