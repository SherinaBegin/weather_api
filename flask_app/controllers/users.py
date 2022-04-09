from flask_app import app 
from flask import render_template, redirect, request, session
import requests

user_api = '40408a7aefab83673e1733945333c46e'


@app.route('/')
def index():
   return render_template('weather.html')


#CREATE user controller
@app.route('/weather/search', methods=['POST'])
def get_weather(): 
   city = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={request.form["city"]}&appid={user_api}').json()
   print(city)
   return render_template('weather.html', city = city)