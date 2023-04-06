from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class ElementLocators():
    def locate_by_idandname(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.NAME,"login-input").send_keys("Ganesh@abc.com")
findbyname = ElementLocators()
findbyname.locate_by_idandname()

