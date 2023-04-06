from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DisabledEnabled():
    def _disable_enable(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://training.openspan.com/login")
        disabled = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(disabled)

        driver.find_element(By.XPATH, "//input[@id='user_name']").send_keys("userganesh")
        driver.find_element(By.XPATH,"//input[@id='user_pass']").send_keys("passwordganesh")
        enabled = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(enabled)

disabledenabled = DisabledEnabled()
disabledenabled._disable_enable()