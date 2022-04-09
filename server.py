from flask_app import app
from flask_app.controllers import users



if __name__=="__main__":
   app.run(debug=True, port = 5001)


# import requests
# import os
# from datetime import datetime

# user_api = '40408a7aefab83673e1733945333c46e'
# location = input ('Enter The City Name: ')

# complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q= "+ location +"&appid="+ user_api

# api_link = requests.get(complete_api_link)
# api_data = api_link.json()


# if api_data['cod'] == '404':
#    print('Invalid City {}, Please check your City namer'.format(location))
# else:
#    # create variables to store and display data
#    temp_city = (api_data['main']['temp'])
#    weather_desc = (api_data['weather'][0]['description'])
#    humdt = api_data['main']['humidity']
#    wind_speed = api_data['wind']['speed']
#    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

# print ("-------------------------------------------------------------")
# print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
# print ("-------------------------------------------------------------")

# print ("Current temperature is: {:.2f} deg C".format(temp_city))
# print ("Current weather desc  :",weather_desc)
# print ("Current Humidity      :",humdt, '%')
# print ("Current wind speed    :",wind_speed ,'kmph')