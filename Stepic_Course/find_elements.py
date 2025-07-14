# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     form = browser.find_elements (By.CLASS_NAME,"first_block")
#     for element in elements:
#         element.send_keys("my answer")                                  

#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")

# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# # не забываем оставить пустую строку в конце файла



from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/find_xpath_form")
    
    elements = driver.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
    for element in elements:
        element.send_keys("Текст")
    
    button = driver.find_element(By.XPATH,'/html/body/div/form/div[6]/button[3]')
    button.click()

finally:
    time.sleep(30)
    driver.quit()