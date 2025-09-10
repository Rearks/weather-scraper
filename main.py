from Skrapper import get_today_weather
import csv
from datetime import datetime
import pandas as pd
import os

def save_data(day, temp, filename="weather1.csv"):
    file_exists = os.path.exists(filename)

    with open(filename, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:  # если файла не было
            writer.writerow(["timestamp", "date", "temp"])
        writer.writerow([datetime.now().isoformat(), day, temp])


def main():
    result = get_today_weather()
    if result is not None:
        day, temp = result
        save_data(day, temp)
        print(f"Получена температура: {temp}")
    else:
        print("Не удалось получить данные о погоде")



    print(f"Сохранено: {day} - {temp}")

if __name__ == "__main__":
    main()
