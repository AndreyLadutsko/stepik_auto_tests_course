# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# try: 
#     link = "http://suninjuly.github.io/registration1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)

#     # Ваш код, который заполняет обязательные поля
#     required_field = browser.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
#     for element in required_field:
#         element.send_keys("Текст")

#     # Отправляем заполненную форму
#     button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
#     button.click()

#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)

#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text

#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text

# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()



from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# WebDriverWait to wait until elements are loaded
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element(By.CSS_SELECTOR, '.first_block .form-group.first_class input')
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.CSS_SELECTOR, '.first_block .form-group.second_class input')
    last_name.send_keys("Bobancki")

    email = browser.find_element(By.CSS_SELECTOR, '.first_block .form-group.third_class input')
    email.send_keys("IvanDogIncDotCom")
    

    # Отправляем заполненную форму
    # button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # button.click()

    # checking
    # waiting till loading needed element and returning error in case if failed
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
except Exception as e:
    print(f"An error occurred: {e}")

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# def fill_field(browser, selector, value):
#     field = browser.find_element(By.CSS_SELECTOR, selector)
#     field.send_keys(value)

# try:
#     link = "http://suninjuly.github.io/registration1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)

#     # Заполняем обязательные поля с помощью CSS-селекторов
#     fill_field(browser, ".first_block .first_class input", "Ivan")
#     fill_field(browser, ".first_block .second_class input", "Bobancki")
#     fill_field(browser, ".first_block .third_class input", "ivan@example.com")

#     # Отправляем форму
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()

#     # Ожидаем появления заголовка
#     welcome_text_elt = WebDriverWait(browser, 5).until(
#         EC.presence_of_element_located((By.TAG_NAME, "h1"))
#     )
#     welcome_text = welcome_text_elt.text

#     assert welcome_text == "Congratulations! You have successfully registered!"

# except Exception as e:
#     print(f"Test failed: {e}")

# finally:
#     browser.quit()

