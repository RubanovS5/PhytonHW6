from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Chrome_driver = webdriver.Chrome()
waiter = WebDriverWait(Chrome_driver, 40)

Chrome_driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

img_locator= (By.ID,"landscape")

img = waiter.until(
    EC.element_to_be_clickable(img_locator))

t = Chrome_driver.find_element(By.CSS_SELECTOR,'img[alt="award"]').get_attribute("src")
print(t)

Chrome_driver.quit()