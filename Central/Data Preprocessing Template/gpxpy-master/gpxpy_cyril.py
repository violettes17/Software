# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 18:46:10 2017

@author: Cyril
"""
# se mettre dans l'environnement weather_py36
# D:\violettes\Software\Central\Data Preprocessing Template\gpxpy-master

import gpxpy
import gpxpy.gpx

# Parsing an existing file:
# -------------------------

gpx_file = open('34.gpx', 'r')

gpx = gpxpy.parse(gpx_file)

for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            print ('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))
