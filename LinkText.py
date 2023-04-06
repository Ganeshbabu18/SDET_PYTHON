import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class LinkText():
    def find_by_linktext(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.find_element(By.PARTIAL_LINK_TEXT, "Holid").click()
        driver.maximize_window()
        time.sleep(4)
findbylinktext = LinkText()
findbylinktext.find_by_linktext()