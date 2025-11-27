import requests

API_KEY = "YOUR_API_KEY"   # Replace with your OpenWeather API Key

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url).json()

    if res["cod"] != 200:
        print("City not found!")
        return

    print("City:", res["name"])
    print("Temperature:", res["main"]["temp"], "°C")
    print("Weather:", res["weather"][0]["description"])

if __name__ == "__main__":
    city = input("Enter city: ")
    get_weather(city)
