import pandas as pd
import matplotlib.pyplot as plt

def analyze_weather(filename="weather1.csv"):
    with open("weather1.csv", "r", encoding="utf-8") as f:
        df = pd.read_csv(filename)
    # строим график
    plt.figure(figsize=(8, 4))
    plt.plot(df["date"], df["temp"], marker="o")
    plt.title("Динамика температуры за дни")
    plt.xlabel("Дата")
    plt.ylabel("Температура °C")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("weather_trend.png")
    plt.close()

    print("weather_trend.png")
if __name__ == "__main__":
    analyze_weather()
