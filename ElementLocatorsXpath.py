from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class ElementLocatorsXpath():
    def locate_by_xpath(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.XPATH, "//*[@id='login-input']").send_keys("ganesh1@mail.com")
findbyxpath = ElementLocatorsXpath()
findbyxpath.locate_by_xpath()