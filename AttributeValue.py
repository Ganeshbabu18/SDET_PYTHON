from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class AttributeValue():
    def attribute_value(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.netmeds.com/")
        att_val = driver.find_element(By.XPATH, "//img[@title='Upto 60% off on Ambitech']").get_attribute("title")
        print(att_val)
attributeandvalue = AttributeValue()
attributeandvalue.attribute_value()
