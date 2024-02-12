from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Chrome_driver = webdriver.Chrome()
waiter = WebDriverWait(Chrome_driver, 20)

Chrome_driver.get("http://uitestingplayground.com/ajax")

waiter.until(EC.element_to_be_clickable((By.ID, "ajaxButton"))).click()

print(waiter.until(EC.visibility_of_element_located((By.XPATH, "//p[@class = 'bg-success']"))).text)
Chrome_driver.quit()