from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time 

try: 
# Open browser
    link = "http://suninjuly.github.io/find_link_text" 
    browser = webdriver.Chrome() # opens Chrome browser
    browser.get(link) # loads the webpage from the link attribute 

# Find an element and interact with it
    link_result = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link_result.click()

# Fill out form
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, '.form-control.city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally: # Close browser
    time.sleep(5)
    browser.quit() # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла



