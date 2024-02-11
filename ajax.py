from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Chrome_driver = webdriver.Chrome()
waiter = WebDriverWait(Chrome_driver, 40)

Chrome_driver.get("http://uitestingplayground.com/ajax")

button_locator = (By.ID, "ajaxButton")

blue_button = waiter.until(EC.element_to_be_clickable(button_locator))
blue_button.click()

green_locator = (By.XPATH, "//p[@class = 'bg-success']")

green_text = waiter.until(EC.visibility_of_element_located(green_locator)).text

print(green_text)

Chrome_driver.quit()
