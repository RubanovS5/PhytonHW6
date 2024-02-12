from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Chrome_driver = webdriver.Chrome()
waiter = WebDriverWait(Chrome_driver, 40)

Chrome_driver.get("http://uitestingplayground.com/textinput")

input_locator = (By.ID, "newButtonName")
input = waiter.until(EC.visibility_of_element_located(input_locator))
input.send_keys("SkyPro")


button_locator = (By.CSS_SELECTOR, ".btn-primary")
blue_button = waiter.until(EC.element_to_be_clickable(button_locator))
blue_button.click()


button_text_locator = (By.XPATH, "//button[@id = 'updatingButton']")
button_text = waiter.until(EC.visibility_of_element_located(button_text_locator)).text
print(button_text)


Chrome_driver.quit()


