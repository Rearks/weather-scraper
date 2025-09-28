from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os


def get_today_weather(url="https://www.yr.no/en/forecast/daily-table/2-524901/Russia/Moscow/Moscow"):
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')

    if 'PYTHONANYWHERE_DOMAIN' in os.environ:
        driver = webdriver.Chrome(options=options)
    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(url)

        # Ждем загрузки блока с текущими условиями
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "now-hero__next-hour-content"))
        )

        # Ищем температуру в блоке текущих условий
        temp_element = driver.find_element(By.CLASS_NAME, "now-hero__next-hour-temperature-text")
        temp_raw = temp_element.text
        temp_number = temp_raw.replace('°', '')
        if not temp_number.startswith('-'):
            temp_final = '+' + temp_number
        else:
            temp_final = temp_number


        day = datetime.now().strftime("%Y-%m-%d")
        print("Текущая температура:", temp_final)
        return day, temp_final

    finally:
        driver.quit()