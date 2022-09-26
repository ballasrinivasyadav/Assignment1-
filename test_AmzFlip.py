import time
import pytest
from selenium.webdriver.common.by import By
from PageObjectModels.ConfirmPage import CheckOutPage
from PageObjectModels.HomePage import HomePage

@pytest.mark.usefixture()
class Test_One:
    def test_one(self,setup):
        homepage = HomePage(self.driver)
        # homepage.gethomepage()
        # time.sleep(2)
        confirm = CheckOutPage(self.driver)
        # confirm.getconfirmpage()
        #
        # time.sleep(4)
        # price1 = confirm.getclickrpage()
        # print(price1)
        # time.sleep(5)




        self.driver.get("https://www.flipkart.com/")
        homepage.getfliphomepage()
        confirm.getflipconfirmpage()
        confirm.getflipkartenter()
        # self.driver.find_element(By.XPATH,"//div[normalize-space()='APPLE iPhone 13 (Starlight, 128 GB)']").click()

        # price2 = self.driver.find_element(By.XPATH, "//div[@class='_30jeq3 _16Jk6d']").text
        price2 = confirm.getclickflipkart()
        print(price2)
        # if price1 < price2:
        #     print("Buy from Amazon")
        # else:
        #     print("Buy from Flipkart")

