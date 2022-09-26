from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self,driver):
        self.driver = driver
    home = (By.XPATH,"//input[@id='twotabsearchtextbox']")
    fliphome = (By.XPATH,"//input[@class='_3704LK']")
    def gethomepage(self):
        self.driver.find_element(*HomePage.home).send_keys("iphone xr 64gb yellow")

    def getfliphomepage(self):
        self.driver.find_element(*HomePage.fliphome).send_keys("iphone")



