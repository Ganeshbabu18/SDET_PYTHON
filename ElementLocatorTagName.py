import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class ElementLocatorTagName():
    def find_by_classname(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        # driver.find_element(By.TAG_NAME, "input").send_keys("gan008@gmal.com")
        driver.find_element(By.CLASS_NAME, "email-login-box").send_keys("gan018@gmal.com")
        time.sleep(3)
# findbytag = ElementLocatorTagName()
# findbytag.find_by_tagname()
findbyclassname = ElementLocatorTagName()
findbyclassname.find_by_classname()