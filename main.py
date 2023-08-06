import tkinter as tk
from tkinter import messagebox
import requests

def get_weather():
    city = city_entry.get()
    api_key = "ca75f9a54f4ea44334967e5c5e06cba3"

    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "units": "metric",
        "appid": api_key,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        location_label.config(text="Location: " + data["name"])
        weather_label.config(text="Weather: " + data["weather"][0]["description"].capitalize())
        temp_label.config(text="Temperature: " + str(data["main"]["temp"]) + " °C")
    else:
        messagebox.showerror("Error", "Failed to fetch weather data. Status code: " + str(response.status_code))

window = tk.Tk()
window.title("Weather App")
window.minsize(width=400, height=300)
window.config(bg="#44B3C5")

label = tk.Label(text="Enter the name of the City" ,bg="#44B3C5", font=("Helvetica", 12))
label.place(x=100, y=25)

city_entry = tk.Entry(width=30)
city_entry.place(x=100, y=60)

search_button = tk.Button(text="Click Here", command=get_weather)
search_button.place(x=150, y=120)

location_label = tk.Label(text="",bg="#44B3C5", font=("Helvetica", 12))
location_label.place(x=100, y=175)

weather_label = tk.Label(text="",bg="#44B3C5", font=("Helvetica", 12))
weather_label.place(x=100, y=200)

temp_label = tk.Label(text="",bg="#44B3C5", font=("Helvetica", 12))
temp_label.place(x=100, y=225)

window.mainloop()