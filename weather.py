import requests
from dotenv import load_dotenv
import os

location = "Clemson"

def getTemp():
    load_dotenv()
    key = os.getenv("API_KEY")
    
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + key
    response = requests.get(url)
    data = response.json()
    temp_kelvin = data['main']['temp']
    temp_fahrenheit = (((temp_kelvin - 273.15) * 9/5 ) + 32)
    return(temp_fahrenheit)


    