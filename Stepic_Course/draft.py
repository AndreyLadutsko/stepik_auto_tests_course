# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome()
# driver.get("https://suninjuly.github.io/explicit_wait2.html")

# # Список интересующих элементов с их локаторами
# elements_to_check = {
#     "price": (By.ID, "price"),
#     "book": (By.ID, "book"),
#     "input_value": (By.ID, "input_value"),
#     "answer": (By.ID, "answer"),
#     "solve": (By.ID, "solve"),
# }

# # Явное ожидание появления всех элементов в течение 15 секунд
# for name, locator in elements_to_check.items():
#     try:
#         element = WebDriverWait(driver, 15).until(EC.presence_of_element_located(locator))
#         print(f"Элемент '{name}' найден.")
#         text = element.text.strip()
#         if text:
#             print(f" элемент '{name}' содержит текст: '{text}'")
#     except Exception as e:
#         print(f"[ОШИБКА] Элемент '{name}' не найден: {str(e)}")

# driver.quit()



#############################################################################################


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://suninjuly.github.io/explicit_wait2.html")

try:
    # Ждём полной загрузки DOM
    WebDriverWait(driver, 15).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )
    print("✅ Страница полностью загружена.")

    # Получаем все элементы в DOM
    all_elements = driver.find_elements(By.XPATH, "//*")
    print(f"🔍 Найдено элементов: {len(all_elements)}")

    for elem in all_elements:
        try:
            tag = elem.tag_name
            classes = elem.get_attribute("class")
            text = elem.get_attribute("textContent").strip()
            output = f"— Элемент: <{tag}>"
            if classes:
                output += f", class='{classes}'"
            if text:
                output += f" → текст: '{text}'"
            print(output)
        except Exception as inner_err:
            print(f"[⚠️ Ошибка обработки элемента]: {str(inner_err)}")

except Exception as outer_err:
    print(f"[❌ Ошибка загрузки страницы или доступа к DOM]: {str(outer_err)}")

driver.quit()
