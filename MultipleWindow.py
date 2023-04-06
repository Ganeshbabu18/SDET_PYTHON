import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class MultipleWindow():
    def muliple_window(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        parent_handle = driver.current_window_handle
        print(parent_handle)
        driver.find_element(By.XPATH, "//img[@alt='Flat 12% OFF (up to Rs 1,500)']").click()
        time.sleep(3)
        all_handle = driver.window_handles
        print(all_handle)
        for handle in all_handle:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                time.sleep(3)
                driver.find_element(By.XPATH, "//a[@id='twtr_yttkd']").click()
                time.sleep(3)
                driver.close()
                time.sleep(3)
                break

        driver.switch_to.window(parent_handle)
        time.sleep(3)
        driver.find_element(By.XPATH, "//img[@alt='Flat 12% OFF (up to Rs 1,500)']").click()
        time.sleep(3)

multiplewindows = MultipleWindow()
multiplewindows.muliple_window()