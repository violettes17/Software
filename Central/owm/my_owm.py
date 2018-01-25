# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 21:36:59 2017

@author: Cyril
"""
# doc https://pyowm.readthedocs.io/en/latest/
# doc https://github.com/csparpa/pyowm/blob/master/pyowm/docs/usage-examples.md
import pyowm

owm = pyowm.OWM('f20e1afb114d39a7c88d271d70dedaef')  # You MUST provide a valid API key

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Will it be sunny tomorrow at this time in Milan (Italy) ?
forecast = owm.daily_forecast("Milan,it")
tomorrow = pyowm.timeutils.tomorrow()
forecast.will_be_sunny_at(tomorrow)  # Always True in Italy, right? ;-)

# Search for current weather in London (UK)
observation = owm.weather_at_place('London,uk')
w = observation.get_weather()
print(w)                      # <Weather - reference time=2013-12-18 09:20,
                              # status=Clouds>

# Weather details
w.get_wind()                  # {'speed': 4.6, 'deg': 330}
w.get_humidity()              # 87
w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
observation_list = owm.weather_around_coords(-22.57, -43.12)
print(observation_list)
observation_list = owm.three_hours_forecast_at_coords(-22.57, -43.12)
time1 = "2017-09-21 11:00:00+00"# ``YYYY-MM-DD HH:MM:SS+00``
time2 = "2017-09-21 18:00:00+00"# ``YYYY-MM-DD HH:MM:SS+00``
w1= observation_list.get_weather_at(time1)
w2= observation_list.get_weather_at(time2)

print(w1.get_temperature())  
print(w2.get_temperature())  

