import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    """Calculate the math function as per instructions."""
    return str(math.log(abs(12 * math.sin(float(x)))))

# Open browser and navigate to the page
driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/execute_script.html")
driver.maximize_window()

try:
    # Find the value x on the page
    x_element = driver.find_element(By.ID, "input_value")
    x = x_element.text  # Retrieve value as string

    # Calculate using the provided formula
    result = calc(x)

    # Input result into the answer field
    answer_input = driver.find_element(By.ID, "answer")
    answer_input.send_keys(result)


    driver.execute_script("window.scrollBy(0, 300);")
    
    select_checkbox_true = driver.find_element(By.CSS_SELECTOR,"[for='robotCheckbox']")
    select_checkbox_true.click()

    radio_button_for_robots = driver.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio_button_for_robots.click()


    
    click_button_submit = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
    # driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    click_button_submit.click()
    


  

finally:
    time.sleep(10)
    driver.quit()
