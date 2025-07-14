from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "https://strategicedgebi.com/"

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(link)

    # Явное ожидание элемента ввода email (до 10 секунд)
    wait = WebDriverWait(driver, 10)
    
    fill_input_email = wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR,
        'input[type="email"]'
    )))
    fill_input_email.send_keys("andrey.ladutsko@365smartshop.com")

    fill_input_password = wait.until(EC.presence_of_element_located((
        By.CSS_SELECTOR,
        'input[type="password"]'
    )))
    fill_input_password.send_keys("Password123!QWE!")

    click_button_login = wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR,
        'button[type="submit"]'
    )))
    click_button_login.click()

    time.sleep(5)  # просто чтобы увидеть результат

finally:
    driver.quit()