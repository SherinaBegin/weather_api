from flask_app import app
from flask_app import keys #importing api_key
from flask import render_template, request
import requests #requests data from API



# rendering page & pulling information from API
@app.route('/')
def index():
   results = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=bellevue&appid={keys.weather}').json()
   print(results)
   # creating dictionary to easily access information from API
   bellevue = {
      'name': results['name'],
      'current_temp': results['main']['temp'],
      'icon': results['weather'][0]['icon'],
      'description': results['weather'][0]['description']
   }
   results1 = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=austin&appid={keys.weather}').json()
   austin = {
      'name': results1['name'],
      'current_temp': results1['main']['temp'],
      'icon': results1['weather'][0]['icon'],
      'description': results1['weather'][0]['description']
   }
   results2 = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=boston&appid={keys.weather}').json()
   boston = {
      'name': results2['name'],
      'current_temp': results2['main']['temp'],
      'icon': results2['weather'][0]['icon'],
      'description': results2['weather'][0]['description']
   }
   return render_template('weather.html', bellevue = bellevue, austin = austin, boston = boston)


#Sending request to database for current information
@app.route('/weather/search', methods=['POST'])
def get_current_weather(): 
   city = request.form['city']
   results = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={keys.weather}').json()   
   print(results)
   return render_template('weather.html', city = results)