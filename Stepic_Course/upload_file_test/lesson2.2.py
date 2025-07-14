import os 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
file_path = "C:\\Users\\andre\\Projects\\VSC Projects\\vAPI\\Stepic_Course\\upload_file_test\\file.txt"
# Проверка перед запуском
print("Путь к файлу:", file_path)
print("Файл найден:", os.path.exists(file_path))       # True, если файл существует

try:
    driver = webdriver.Chrome()
    driver.get(link)
    driver.maximize_window()

    # Заполнение формы
    input_firstname = driver.find_element(By.NAME, "firstname")
    input_firstname.send_keys("Ivan")

    input_lastname = driver.find_element(By.NAME, "lastname")
    input_lastname.send_keys("Ivan")

    input_email = driver.find_element(By.NAME, "email")
    input_email.send_keys("Ivan")

    # Загрузка файла
    
    driver.find_element(By.ID, "file").send_keys(file_path)
    driver.find_element(By.CLASS_NAME, "btn").click()


finally:
    time.sleep(10)
    driver.quit()
