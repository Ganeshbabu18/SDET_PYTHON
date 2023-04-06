import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class ElementLocatorCssSelector():
    def find_by_cssselector(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.CSS_SELECTOR, "#login-input").send_keys("ganesh1@mail.com")
        time.sleep(4)
findbycss = ElementLocatorCssSelector()
findbycss.find_by_cssselector()
