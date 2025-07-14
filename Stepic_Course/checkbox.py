from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

link = "https://suninjuly.github.io/math.html"


def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) #formula for calc


# open browser
browser = webdriver.Chrome()
browser.get(link)


try:
    x_element = browser.find_element(By.ID, "input_value") #calc based on the formula 
    x = x_element.text
    y = calc(x)

#input answer
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

#selecting check box
    checkbox_for_robot = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    checkbox_for_robot.click()
#selecting radiobutton
    radio_button_for_robots = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radio_button_for_robots.click()
#click on Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_button.click()


    time.sleep(10)

finally:

#wait to see result
    time.sleep(10)
    browser.quit()
