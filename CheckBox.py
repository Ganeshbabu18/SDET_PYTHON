import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class CheckBox():
    def check_box(self):

        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.leafground.com/checkbox.xhtml;jsessionid=node01wa1jl3j4fpo93ol047pe0xcg192484.node0")
        driver.maximize_window()
        driver.find_element(By.XPATH,"//*[@id='j_idt87:basic']/tbody/tr/td[1]/div/div[2]").click()
        print(driver.find_element(By.XPATH,"//*[@id='j_idt87:basic']/tbody/tr/td[1]/div/div[2]").is_selected())
        driver.find_element(By.XPATH,"//*[@id='j_idt87:basic']/tbody/tr/td[3]/div/div[2]").click()
        print(driver.find_element(By.XPATH,"//*[@id='j_idt87:basic']/tbody/tr/td[3]/div/div[2]").is_selected())
        time.sleep(3)

Checkboxedemo = CheckBox()
Checkboxedemo.check_box()