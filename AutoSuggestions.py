import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class AutoSuggestions():
    def auto_suggestions(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        autoss = driver.find_element(By.ID, "BE_flight_origin_city")
        autoss.click()
        time.sleep(3)
        autoss.send_keys("Chennai")
        time.sleep(3)
        autoss.send_keys(Keys.ENTER)
        time.sleep(3)

        autoss2 = driver.find_element(By.XPATH, "//*[@id='BE_flight_arrival_city']")
        autoss2.send_keys("New")
        searching = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]//li")
        print(len(searching))
        time.sleep(3)
        for results in searching:
            print(results.text)
            time.sleep(3)
            if "New York (JFK)" in results.text:
                results.click()
                time.sleep(3)
                break

autosugg = AutoSuggestions()
autosugg.auto_suggestions()