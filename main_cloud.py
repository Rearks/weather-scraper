import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import os
from google.cloud import storage


def get_weather_data():
    url = "https://www.yr.no/en/forecast/daily-table/2-524901/Russia/Moscow/Moscow"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        temp_element = soup.find('div', class_='now-hero__next-hour-temperature-text')

        if temp_element:
            temp_text = temp_element.text.strip()
            day = datetime.now().strftime("%Y-%m-%d")
            return day, temp_text
    return None


def weather_scraper(request):
    """Cloud Function entry point"""
    result = get_weather_data()
    if result:
        day, temp = result
        print(f"Собрана температура: {day} - {temp}")
        return f"Получено: {day} - {temp}"
    else:
        return "Не удалось загрузить"