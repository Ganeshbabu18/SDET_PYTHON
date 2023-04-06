import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class alertsPP():
    def alert_pp(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.maximize_window()
        driver.switch_to.frame("iframeResult")

        # # Alert accept - okay
        # driver.find_element(By.XPATH, "//button[@onclick='myFunction()']").click()
        # time.sleep(3)
        # driver.switch_to.alert.accept()
        # time.sleep(3)
        #
        # # Alert dismiss - cancel
        # driver.find_element(By.XPATH, "/html/body/button").click()
        # time.sleep(3)
        # driver.switch_to.alert.dismiss()
        # time.sleep(2)

        # Alert Text
        driver.find_element(By.XPATH, "/html/body/button").click()
        time.sleep(3)
        driver.switch_to.alert.send_keys("Ganesh Babu")
        time.sleep(3)
        driver.switch_to.alert.accept()
        time.sleep(2)


alerts = alertsPP()
alerts.alert_pp()

