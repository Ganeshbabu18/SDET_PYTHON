import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class iFrames():
    def i_frames(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='iframeResult']"))
        driver.switch_to.frame(0)
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@id='signupbtn_topnav']").click()
        time.sleep(3)

iframes = iFrames()
iframes.i_frames()