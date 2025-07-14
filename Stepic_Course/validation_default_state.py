# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time 
# import math

# link = "https://suninjuly.github.io/math.html"


# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x))))) #formula for calc


# # open browser
# browser = webdriver.Chrome()
# browser.get(link)

# try:
#     x_element = browser.find_element(By.ID, "input_value") #calc based on the formula 
#     x = x_element.text
#     y = calc(x)

# #check the dafault state of the People radiobutton, returns error
#     people_radio = browser.find_element(By.ID, "peopleRule")
#     people_checked = people_radio.get_attribute("checked")
#     print("value of people radio: ", people_checked)
#     assert people_checked == "false", "People radio is  selected by default"
#     time.sleep(10)

#     submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
#     submit_button_state = submit_button.get_attribute ("disabled")  
#     print("submit_button_state:", submit_button_state)
#     assert submit_button_state == "true", "submit_button_state is disabled"
#     time.sleep(10)
   

    
# finally:

# #wait to see result
#     time.sleep(10)
#     browser.quit()




from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


link = "https://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    # Проверка состояния радиокнопки People Rule
    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio:", people_checked)
    
    assert people_checked == "true", "People radio is unselected by default"

    # Пауза 10 секунд перед проверкой кнопки Submit
    time.sleep(15)

    submit_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit_button_state = submit_button.get_attribute("disabled")
    print("submit_button_state:", submit_button_state)
    
    assert submit_button_state == "true", "Submit button should be disabled by default"

    time.sleep(5)

finally:
    browser.quit()
