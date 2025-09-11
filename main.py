from Skrapper import get_today_weather
import csv
from datetime import datetime
import os
import schedule
import time

def save_data(day, temp, filename="weather1.csv"):
    file_exists =  os.path.exists(filename)
    with open(filename, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp", "date", "temp"])
        writer.writerow([datetime.now().isoformat(), day, temp])

def collect_and_save():
    result = get_today_weather()
    if result is not None:
        day, temp = result
        save_data(day, temp)
        print(f"Сохранено: {day} - {temp}")
    else:
        print("Не удалось получить данные о погоде")

# Планируем задачу
schedule.every().day.at("10:00").do(collect_and_save)

if __name__ == "__main__":
    print("Планировщик запущен. Сбор данных каждый день в 10:00")
    while True:
        schedule.run_pending()
        time.sleep(60)