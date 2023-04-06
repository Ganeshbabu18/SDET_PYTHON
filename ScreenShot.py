from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class ScreenShot():
    def screen_shot(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")

        scnsht = driver.find_element(By.XPATH, "//*[@id='login-continue-btn']")
        scnsht.screenshot(".\\TestSCC.png")
        scnsht.click()

        driver.get_screenshot_as_file("C:\\Python Selenium\\ErrorSC1.png")
        driver.save_screenshot(".\\TestSC2.png")

screenshot = ScreenShot()
screenshot.screen_shot()