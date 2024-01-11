import requests
import os
from datetime import datetime

user_api=os.environ['current_weather_data']
location=input("Enter the city name  :")


complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

api_link=requests.get(complete_api_link)
api_data=api_link.json()

if api_data['cod']=='404':
    print("Invalid city please enter a valid city ")

else:
    temp_of_city=((api_data['main']['temp'])-273.15)  # from main function give me temp
    weather_des=api_data['weather'][0]['description']  # from weather need description-like clear sky
    humid=api_data['main']['humidity']
    wind_speed=api_data['wind']['speed']
    date_time=datetime.now().strftime("%d %b %Y | %I: %M :%S %p") #string format for date and time
    
    
    print("************************************************")
    print("Weather stats for-{}  || {}".format(location.upper(),date_time))
    print("************************************************")
    
    print("Current temperature is:{:.2f} deg c".format(temp_of_city))
    print("Current weather description :", weather_des)
    print("Current Humidity:", humid, "%")
    print("Current wind speed:", wind_speed, "kmph")