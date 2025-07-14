import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException

link = "https://suninjuly.github.io/redirect_accept.html"

def calc(x):
    """Calculate the math function as per instructions."""
    return str(math.log(abs(12 * math.sin(float(x)))))



try:
    # Open browser and navigate to the page
    driver = webdriver.Chrome()
    driver.get(link)
    driver.maximize_window()

    # Input result into the answer field
    click_magic_button = driver.find_element(By.TAG_NAME, "button")
    click_magic_button.click()

    window_name = driver.window_handles[1] # this line gets all opened tabs, in this case 'window_name ' variable = browser tab that is counted as '1' (counting starts from '0') 
    driver.switch_to.window(window_name) # this methow switches test to another browser tab, where first tab counted as '0', second tab counted as '1'

  

    # Find the value x on the page
    x_element = driver.find_element(By.ID, "input_value")
    x = x_element.text  # Retrieve value as string

    # Calculate using the provided formula
    result = calc(x)

    # oput answer into field
    fill_result = driver.find_element(By.ID, "answer")
    fill_result.send_keys(result)
    
    click_button_submit = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
    click_button_submit.click()
     

finally:
    time.sleep(10)
    driver.quit()
