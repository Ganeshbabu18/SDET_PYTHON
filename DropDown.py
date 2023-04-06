import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


class DropDown():
    def drop_down(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
        Dropdwn = driver.find_element(By.XPATH,"//*[@id='post-2646']/div[2]/div/div/div/p/select")
        time.sleep(3)
        dd = Select(Dropdwn)

        dd.select_by_index(1)
        time.sleep(3)
        dd.select_by_value("NAM")
        time.sleep(3)
        dd.select_by_visible_text("Albania")
        time.sleep(3)

dddropdown = DropDown()
dddropdown.drop_down()