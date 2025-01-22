import time
import pandas as pd
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
pass 

# Загрузка данных из Excel
file_path = r"D:\safe gitt\Vbivalka\venv\Для заполнение карточки.xlsx"  # Укажите путь к файлу
data = pd.read_excel(file_path)

# Настройка Selenium
options = webdriver.FirefoxOptions()  # Правильная инициализация объекта options для Firefox
driver = webdriver.Firefox(options=options)  # Создание драйвера с опциями
driver.get("https://www.google.com/search?q=")  # Укажите URL сайта

# Перебор строк из Excel
for index, row in data.iterrows():
    try:
        print(row["Имя"])
        # Найдите элементы на сайте и заполните их
        name_field = driver.find_element(By.ID, "APjFqb")
        ##email_field = driver.find_element(By.ID, "email_field_id")  # Замените на актуальный ID
        ##phone_field = driver.find_element(By.ID, "phone_field_id")  # Замените на актуальный ID

        # Заполнение полей
        name_field.clear()
        name_field.send_keys(row["Имя"])
        
        
        ##email_field.clear()
        ##email_field.send_keys(row["Email"])

        ##phone_field.clear()
        ##phone_field.send_keys(row["Телефон"])

        # Если нужно нажать кнопку "Отправить"
        ##submit_button = driver.find_element(By.ID, "submit_button_id")  # Замените на актуальный ID
        ##submit_button.click()

        # Ждем, чтобы избежать блокировки
        time.sleep(2)

    except Exception as e:
        print(f"Ошибка на строке {index}: {e}")
pyautogui.press('enter')
# Закрыть браузер
##driver.quit()