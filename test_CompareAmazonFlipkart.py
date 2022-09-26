import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# driver = webdriver.Chrome("C:\\Users\\Srinivas\\PycharmProjects\\Assignment1\\Driver\\chromedriver.exe")
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# driver.implicitly_wait(20)
from PageObjectModels.ConfirmPage import CheckOutPage
from PageObjectModels.HomePage import HomePage


@pytest.mark.usefixtures()
class TestCompare:

    def testcompare(self,setup):
        home = HomePage(self.driver)
        home.gethomepage()

        # self.driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("iphone xr 64gb yellow")
        time.sleep(2)
        confirm = CheckOutPage(self.driver)
        confirm.getconfirmpage()

        # self.driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
        time.sleep(4)
        price1 = confirm.getclickrpage()
        # price1 = self.driver.find_element(By.XPATH, "//span[normalize-space()='1,00,900']")
        k = price1
        m = []
        for price in k:
            if price.isdigit() == True:
                m.append(price)
        amazonprice = ''.join(m)
        amazonvalue = int(amazonprice)
        print(amazonvalue)
        print(type(amazonvalue))
        time.sleep(10)

        self.driver.get("https://www.flipkart.com/")
        home.getfliphomepage()
        # self.driver.find_element(By.XPATH, "//input[@class='_3704LK']").send_keys("iphone")
        time.sleep(5)
        confirm.getflipconfirmpage()
        # self.driver.find_element(By.XPATH, "//button[@type='submit']//*[name()='svg']").click()
        time.sleep(10)
        confirm.getflipkartenter()
        # self.driver.find_element(By.XPATH, "//div[normalize-space()='APPLE iPhone 13 (Starlight, 128 GB)']").click()
        p = self.driver.window_handles
        print("parent win :", self.driver.current_window_handle)
        for x in p:
            self.driver.switch_to.window(x)
        print("Child window title :" + self.driver.title)
        time.sleep(2)
        print("Child win : ", self.driver.current_window_handle)
        # val = self.driver.find_element(By.XPATH, "//div[@class='_30jeq3 _16Jk6d']").text
        val = confirm.getclickflipkart().text
        y = []
        for x in val:
            if x.isdigit() == True:
                y.append(x)
        flipkartprice = ''.join(y)
        flipkartvalue = int(flipkartprice)
        print(flipkartvalue)
        print(type(flipkartvalue))

        if flipkartvalue > amazonvalue:
            print(flipkartvalue)
        elif flipkartvalue == amazonvalue:
            print("Both are equal")
        else:
            print(amazonvalue)
