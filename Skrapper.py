from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime





def get_today_weather(url = "https://dzen.ru/pogoda/213"):
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(url)

        print("Страница загружается")

        # Таймер таймаут
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "temp__value.temp__value_with-unit"))
        )

        print("загружается")
        cards = driver.find_elements(By.CLASS_NAME, "forecast-briefly__day")
        day = datetime.now().strftime("%Y-%m-%d")
        for card in cards:
            name = card.find_element(By.CLASS_NAME, "forecast-briefly__name").text
            #print(f"Найдена карточка:", name)
            temp = card.find_element(By.CSS_SELECTOR, ".temp__value.temp__value_with-unit").text
            #print(f"Найдена карточка:", temp)

            if name == "Сегодня":
                print("Сегодня:", temp)
                return day, temp



    finally:
        driver.quit()

#get_today_weather(url = "https://dzen.ru/pogoda/213")

