# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 20:28:36 2017

@author: Cyril
"""

# se mettre dans l'environnement weather_py36
# D:\violettes\Software\Central\Data Preprocessing Template\gpxpy-master

# doc https://pyowm.readthedocs.io/en/latest/
# doc https://github.com/csparpa/pyowm/blob/master/pyowm/docs/usage-examples.md

import gpxpy
import gpxpy.gpx
import pyowm

owm = pyowm.OWM('f20e1afb114d39a7c88d271d70dedaef')  # You MUST provide a valid API key


time1 = "2017-09-22 18:00:00+00"# ``YYYY-MM-DD HH:MM:SS+00``
w1= observation_list.get_weather_at(time1)

# Parsing an existing file:
# -------------------------

gpx_file = open('34.gpx', 'r')  # Mont dore, Auvergne, FRANCE

gpx = gpxpy.parse(gpx_file)

for track in gpx.tracks:    # Various altitude at the same time
    for segment in track.segments:
        for point in segment.points:
            observation_list = owm.three_hours_forecast_at_coords(point.latitude, point.longitude)#(-22.57, -43.12)
            w1= observation_list.get_weather_at(time1)
            dict = w1.get_temperature('celsius')
            #print(dict ['temp_min'])
            print ('Point at ({0},{1}) -> {2}, {3} °C'.format(point.latitude, point.longitude, point.elevation,dict ['temp_min']))
# same temperature :(
# site météo de montgolfière : vitesse de vent et température à différentes altitudes
