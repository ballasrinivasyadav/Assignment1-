
from selenium import webdriver
link = "C:\\Users\\Srinivas\\PycharmProjects\\Assignment1\\Driver\\chromedriver.exe"
driver = webdriver.Chrome(link)
driver.maximize_window()
driver.delete_all_cookies()
urls = ["https://www.amazon.in/","https://www.flipkart.com/","https://www.ebay.com/","https://www.shopify.com/in"]

for posts in range(len(urls)):
        print(posts)
        driver.get(urls[posts])
        if(posts!=len(urls)-1):
                driver.execute_script("window.open('')")
                chwd = driver.window_handles
                driver.switch_to.window(chwd[-1])
chwd = driver.window_handles
print(chwd)


