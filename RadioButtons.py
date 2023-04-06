import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class RadioButtons():
    def radio_buttons(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.leafground.com/radio.xhtml")
        driver.find_element(By.XPATH, "//*[@id='j_idt87:age']/div/div[1]/div/div[2]").click()
        print(driver.find_element(By.XPATH, "//*[@id='j_idt87:age']/div/div[1]/div/div[2]").is_selected())
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='j_idt87:age']/div/div[3]/div/div[2]").click()
        time.sleep(3)

radiobutton = RadioButtons()
radiobutton.radio_buttons()