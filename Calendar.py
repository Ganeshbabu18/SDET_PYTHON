import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Calendar():
    def Auto_sug_calendar(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        ASCalendar = driver.find_element(By.XPATH,"//*[@id='BE_flight_origin_city']")
        ASCalendar.click()
        time.sleep(2)
        ASCalendar.send_keys("Chennai")
        time.sleep(2)
        ASCalendar.send_keys(Keys.ENTER)
        time.sleep(2)

        ASCalendar2 = driver.find_element(By.XPATH, "//*[@id='BE_flight_arrival_city']")
        time.sleep(2)
        ASCalendar2.send_keys("New")
        time.sleep(2)
        goingto = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]//li")
        print(len(goingto))
        time.sleep(2)
        for results in goingto:
            print(results.text)
            if "New York (NYC)" in results.text:
                results.click()
                time.sleep(2)
                break

        Calendar1 = driver.find_element(By.XPATH, "//*[@id='BE_flight_origin_date']")
        Calendar1.click()
        time.sleep(2)

        calendar2 = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td")
        for result in calendar2:
            if result.get_attribute("data-date") == "30/08/2023":
                result.click()
                time.sleep(3)
                break


calendarAS = Calendar()
calendarAS.Auto_sug_calendar()
