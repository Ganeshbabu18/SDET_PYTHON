import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


class MultiDropDown():
    def multi_drop_down(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")
        multidropdwn = driver.find_element(By.XPATH, "//select[@id='second']")
        multidd = Select(multidropdwn)
        time.sleep(3)
        multidd.select_by_index(1)
        multidd.select_by_visible_text("Burger")
        multidd.select_by_value("bonda")
        time.sleep(3)
        multidd.deselect_by_index(1)
        time.sleep(3)
        multidd.deselect_all()
        time.sleep(3)

multidddropdown = MultiDropDown()
multidddropdown.multi_drop_down()