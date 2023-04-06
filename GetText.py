from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class GetText():
    def get_text(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.netmeds.com/")
        text = driver.find_element(By.XPATH, "//a[normalize-space()='Sign in / Sign up']").text
        print(text)
        print(len(text))
gettext = GetText()
gettext.get_text()
