
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:

    driver = webdriver.Chrome()
    driver.get("http://suninjuly.github.io/explicit_wait2.html")

# Ожидаем снижения цены до $100 (макс. ожидание 15 секунд)
    WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    

# Кликаем кнопку "Book"
    driver.find_element(By.ID, "book").click()

# Получаем значение x и решаем задачу
    x = driver.find_element(By.ID, "input_value").text
    answer = calc(x)

# Вводим ответ и отправляем форму
    driver.find_element(By.ID, "answer").send_keys(answer)
    driver.find_element(By.ID, "solve").click()

finally:
    time.sleep(10)
    driver.quit()