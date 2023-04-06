import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class browserMethods():
    def browser_method(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.netmeds.com/")
        driver.maximize_window()
        print(driver.current_url)
        print(driver.title)
        driver.refresh()
        time.sleep(3)
        driver.find_element(By.XPATH, "(//a[@class='m-pro1'])[1]").click()
        time.sleep(3)
        driver.back()
        time.sleep(3)
        driver.forward()
        time.sleep(3)
        driver.minimize_window()
        time.sleep(3)
        driver.quit()

browserido = browserMethods()
browserido.browser_method()